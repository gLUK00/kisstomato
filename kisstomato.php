<?php

	class kisstomato{

		// singleton
		private static $oThis = NULL;
		static function get(){
			if( is_null( self::$oThis ) ){
				self::$oThis = new kisstomato();
			}
			return self::$oThis;
		}

		// merge 2 repertoires
		public function mergeDirs( $sSource, $sModel, &$sDest, &$oExtsTags ){
			
			// pour tous les fichiers du modele
			foreach( scandir( $sModel ) as $sScanDir ){
				if( in_array( $sScanDir, array( '.', '..', '.svn' ) ) ){
					continue;
				}
				
				// determine si c'est un repertoire
				if( is_dir( $sModel.DS.$sScanDir ) ){
					
					// determine si le repertoire existe dans la destination
					if( !file_exists( $sDest.DS.$sScanDir ) ){
						$this->dirsCreate( $sDest.DS.$sScanDir );
					}
					
					// determine si celui-ci existe egalement dans la source
					if( file_exists( $sSource.DS.$sScanDir ) ){
						
						// merge le repertoire
						$SubSource = $sSource.DS.$sScanDir;
						$SubModel = $sModel.DS.$sScanDir;
						$SubDest = $sDest.DS.$sScanDir;
						$this->mergeDirs( $SubSource, $SubModel, $SubDest, $oExtsTags );
					}
					continue;
				}
				
				// determine si le source n'existe pas
				if( !file_exists( $sSource.DS.$sScanDir ) ){
					
					// copie le fichier du modele
					copy( $sModel.DS.$sScanDir, $sDest.DS.$sScanDir );
				}else{

					// recupere l'extension du modele
					$oInfo = pathinfo( $sModel.DS.$sScanDir );
					if( isset( $oInfo[ 'extension' ] ) && array_key_exists( strtolower( $oInfo[ 'extension' ] ), $oExtsTags ) ){

						// recupere les informations de fusion
						$oMergeInfos = $oExtsTags[ $oInfo[ 'extension' ] ];

						// determine si le fichier a une zone de saisie a la derniere ligne
						$sContentModel = file_get_contents( $sModel.DS.$sScanDir );
						$oLines = explode( "\n", $sContentModel );
						$sLastLine = trim( $oLines[ count( $oLines ) - 1 ] );
						$bInsertLastRC = stripos( $sLastLine, $oMergeInfos[ 'stop' ] ) === 0;
						if( $bInsertLastRC ){
							$sContentModel .= "\n";
						}
						
						// merge le modele avec la source
						$iPosBlock = stripos( $sContentModel, $oMergeInfos[ 'start' ] );
						while( $iPosBlock !== false ){

							// recherche le nom de la section
							$iPosNameStop = stripos( $sContentModel, $oMergeInfos[ 'start_end' ], $iPosBlock + strlen( $oMergeInfos[ 'start' ] ) );
							$sSectionName = substr( $sContentModel, $iPosBlock + strlen( $oMergeInfos[ 'start' ] ), $iPosNameStop - ( $iPosBlock + strlen( $oMergeInfos[ 'start' ] ) ) );
							
							// determine le tag START et STOP
							$sTagStart = $oMergeInfos[ 'start' ].$sSectionName.$oMergeInfos[ 'start_end' ];
							$sTagStop = $oMergeInfos[ 'stop' ].$sSectionName.$oMergeInfos[ 'stop_end' ];
							
							// recupere la valeur par defaut du modele
							$iPosTagStop = stripos( $sContentModel, $sTagStop, $iPosBlock ) + strlen( $sTagStop );
							$sValContent = substr( $sContentModel, $iPosBlock, $iPosTagStop - $iPosBlock );
							
							// determine si les tags sont presents dans le fichier source
							$sContentSource = file_get_contents( $sSource.DS.$sScanDir );
							do{
								$iSourcePosStart = stripos( $sContentSource, $sTagStart );
								if( $iSourcePosStart === false ){
									break;
								}
								$iSourcePosStop = stripos( $sContentSource, $sTagStop, $iSourcePosStart + strlen( $sTagStart ) );
								if( $iSourcePosStop === false ){
									break;
								}
								$iSourcePosStop += strlen( $sTagStop );
								
								// recupere le nouveau contenu de la section
								$sValContent = substr( $sContentSource, $iSourcePosStart, $iSourcePosStop - $iSourcePosStart );

							}while( false );						
							
							// mise a jour du contenu
							$sContentModel = substr( $sContentModel, 0, $iPosBlock ).$sValContent.substr( $sContentModel, stripos( $sContentModel, $sTagStop, $iPosNameStop ) + strlen( $sTagStop ) );
							
							// recherche la prochaine position
							$iPosBlock = stripos( $sContentModel, $oMergeInfos[ 'start' ], $iPosBlock + strlen( $oMergeInfos[ 'start' ] ) );
						}

						// supprime le dernier charactere
						if( $bInsertLastRC ){
							$sContentModel = substr( $sContentModel, 0, strlen( $sContentModel ) - 1 );
						}
						
						// creation du nouveau fichier
						file_put_contents( $sDest.DS.$sScanDir, $sContentModel );
						
					// aucune information concernant le merge, copie du fichier du modele
					}else{
						copy( $sModel.DS.$sScanDir, $sDest.DS.$sScanDir );
					}
				}
				@chmod( $sDest.DS.$sScanDir, 0777 );
			
			// fin, foreach des fichiers / repertoires
			}
		}

		// generation d'un fichier a partir d'un template
		public function genFromTemplate( $oData, $sDestFile, $sSrcTemplate ){
			$PHP_TAG = '<?php';
			ob_start();
			include( $sSrcTemplate );
			$sContent = ob_get_clean();
			file_put_contents( $sDestFile, $sContent );
		}

		// supprime un repertoire de maniere recursive
		public function fsRrmdir($dir) {
			if (is_dir($dir)) {
				$objects = scandir($dir);
				foreach ($objects as $object) {
					if ($object != "." && $object != "..") {
						if (filetype($dir.DS.$object) == "dir") $this->fsRrmdir($dir.DS.$object); else unlink($dir.DS.$object);
					}
				}
				reset($objects);
				return @rmdir($dir);
			}
			return true;
		}

		// creation de repertoires
		public function dirsCreate( $oDirs, $bDeleteIfExist = false ){
			$oResult = array();

			if( is_array( $oDirs ) ){
				foreach( $oDirs as $sDir ){
					$oResult = array_merge( $oResult, $this->dirsCreate( $sDir, $bDeleteIfExist ) );
				}
				return $oResult;
			}
			if( $bDeleteIfExist && file_exists( $oDirs ) ){
				$bDelDir = self::$oThis->fsRrmdir( $oDirs );
				if( !$bDelDir ){
					$oError = error_get_last();
					$oResult[] = 'Delete error : '.$oDirs.' : '.$oError[ 'message' ];
				}
			}
			if( !file_exists( $oDirs ) ){
				mkdir( $oDirs, 0777, true );
			}
			return $oResult;
		}

		// camel case sur une chaine
		public function toCamelCase( $sValue ){
			return str_replace( ' ', '', ucwords( str_replace( '_', ' ', $sValue ) ) );
		}
	}
