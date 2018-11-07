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

			// fonction anonyme de recuperation de structure d'un fichier
			$fGetStruct = function( $sPathFile, $oMergeInfos ){
				$oResults = array();

				$sContent = file_get_contents( $sPathFile );
				$iPosBlock = stripos( $sContent, $oMergeInfos[ 'start' ] );
				while( $iPosBlock !== false ){
					$iPosStop = stripos( $sContent, $oMergeInfos[ 'start_end' ], $iPosBlock );
					if( $iPosStop === false ){
						break;
					}
					$sSectionName = substr( $sContent, $iPosBlock, $iPosStop - $iPosBlock );
					$sSectionName = trim( substr( $sSectionName, strlen( $oMergeInfos[ 'start' ] ) ) );
					$iPosStopBlock = stripos( $sContent, $oMergeInfos[ 'stop' ].$sSectionName, $iPosStop );
					if( $iPosStopBlock === false ){
						break;
					}
					$iPosStop += strlen( $oMergeInfos[ 'start_end' ] );
					$oResults[ $sSectionName ] = substr( $sContent, $iPosStop, $iPosStopBlock - $iPosStop );
					$iPosBlock = stripos( $sContent, $oMergeInfos[ 'start' ], $iPosStopBlock );
				}

				return $oResults;
			};
			
			// pour tous les fichiers du modele
			foreach( scandir( $sModel ) as $sScanDir ){
				if( in_array( $sScanDir, array( '.', '..', '.svn' ) ) ){
					continue;
				}
				
				// determine si c'est un repertoire
				if( is_dir( $sModel.DIRECTORY_SEPARATOR.$sScanDir ) ){
					
					// determine si le repertoire existe dans la destination
					if( !file_exists( $sDest.DIRECTORY_SEPARATOR.$sScanDir ) ){
						$this->dirsCreate( $sDest.DIRECTORY_SEPARATOR.$sScanDir );
					}
					
					// determine si celui-ci existe egalement dans la source
					if( file_exists( $sSource.DIRECTORY_SEPARATOR.$sScanDir ) ){
						
						// merge le repertoire
						$SubSource = $sSource.DIRECTORY_SEPARATOR.$sScanDir;
						$SubModel = $sModel.DIRECTORY_SEPARATOR.$sScanDir;
						$SubDest = $sDest.DIRECTORY_SEPARATOR.$sScanDir;
						$this->mergeDirs( $SubSource, $SubModel, $SubDest, $oExtsTags );
					}
					continue;
				}
				
				// determine si le source n'existe pas
				if( !file_exists( $sSource.DIRECTORY_SEPARATOR.$sScanDir ) ){
					
					// copie le fichier du modele
					copy( $sModel.DIRECTORY_SEPARATOR.$sScanDir, $sDest.DIRECTORY_SEPARATOR.$sScanDir );
				}else{

					// recupere l'extension du modele
					$oInfo = pathinfo( $sModel.DIRECTORY_SEPARATOR.$sScanDir );
					if( isset( $oInfo[ 'extension' ] ) && array_key_exists( strtolower( $oInfo[ 'extension' ] ), $oExtsTags ) ){

						// recupere les informations de fusion
						$oMergeInfos = $oExtsTags[ $oInfo[ 'extension' ] ];

						// recupere les informations des structures de la source et du modele
						$oStructSource = $fGetStruct( $sSource.DIRECTORY_SEPARATOR.$sScanDir, $oMergeInfos );
						$oStructModel = $fGetStruct( $sModel.DIRECTORY_SEPARATOR.$sScanDir, $oMergeInfos );

						// alimentation du fichier de model
						$sContentModel = file_get_contents( $sModel.DIRECTORY_SEPARATOR.$sScanDir );
						foreach( $oStructModel as $sSectionName=>$sContent ){
							if( !isset( $oStructSource[ $sSectionName ] ) ){
								continue;
							}

							// recherche de la section a alimenter
							$iPosBlock = stripos( $sContentModel, $oMergeInfos[ 'start' ].$sSectionName.$oMergeInfos[ 'start_end' ] );
							if( $iPosBlock === false ){
								continue;
							}
							$iPosStopBlock = stripos( $sContentModel, $oMergeInfos[ 'stop' ].$sSectionName, $iPosBlock );
							if( $iPosStopBlock === false ){
								continue;
							}

							// remplacement de la section
							$sContentModel = substr( $sContentModel, 0, $iPosBlock ).
								$oMergeInfos[ 'start' ].$sSectionName.$oMergeInfos[ 'start_end' ].
								$oStructSource[ $sSectionName ].
								substr( $sContentModel, $iPosStopBlock );
						}

						// creation du nouveau fichier
						file_put_contents( $sDest.DIRECTORY_SEPARATOR.$sScanDir, $sContentModel );
						
					// aucune information concernant le merge, copie du fichier du modele
					}else{
						copy( $sModel.DIRECTORY_SEPARATOR.$sScanDir, $sDest.DIRECTORY_SEPARATOR.$sScanDir );
					}
				}
				@chmod( $sDest.DIRECTORY_SEPARATOR.$sScanDir, 0777 );
			
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
						if (filetype($dir.DIRECTORY_SEPARATOR.$object) == "dir") $this->fsRrmdir($dir.DIRECTORY_SEPARATOR.$object); else unlink($dir.DIRECTORY_SEPARATOR.$object);
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
