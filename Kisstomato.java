package my.package;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashMap;

import org.apache.commons.io.FileUtils;
import org.apache.commons.io.FilenameUtils;

public class Kisstomato{
	
	// singleton
    private Kisstomato(){}
    private static Kisstomato INSTANCE = null;
    public static synchronized Kisstomato getInstance(){
        if (INSTANCE == null){
        	INSTANCE = new Kisstomato();
        }
        return INSTANCE;
    }
    
    private HashMap<String, String> getStruct(String sPathFile, HashMap<String, String> oMergeInfos) throws IOException{
    	HashMap<String, String> oResults = new HashMap<String, String>();

    	String sContent = new String( Files.readAllBytes( Paths.get( sPathFile ) ) );
    	Integer iPosBlock = sContent.indexOf( oMergeInfos.get( "start" ) );

		while( iPosBlock != -1 ){
			Integer iPosStop = sContent.indexOf( oMergeInfos.get( "start_end" ), iPosBlock );
			if( iPosStop == -1 ){
				break;
			}
			String sSectionName = sContent.substring(iPosBlock, iPosStop );
			sSectionName = sSectionName.substring( oMergeInfos.get( "start" ).length() ).trim();
			
			Integer iPosStopBlock = sContent.indexOf( oMergeInfos.get( "stop" ).concat( sSectionName ), iPosStop );
			if( iPosStopBlock == -1 ){
				break;
			}
			iPosStop += oMergeInfos.get( "start_end" ).length();
			oResults.put( sSectionName, sContent.substring( iPosStop, iPosStopBlock ) );
			iPosBlock = sContent.indexOf( oMergeInfos.get( "start" ), iPosStopBlock );
		}
    	
    	return oResults;
    }

	// merge 2 repertoires
	public void mergeDirs( String sSource, String sModel, String sDest, HashMap<String, HashMap<String, String>> oExtsTags ) throws IOException{
		
		// pour tous les fichiers du modele
		for( File oFile : new File( sModel ).listFiles() ) {

			String sScanDir = oFile.getName();
			if( Arrays.stream(new String[] { ".", "..", ".svn" } ).anyMatch(sScanDir.toLowerCase()::equals) ) {
				continue;
			}
			
			// determine si c'est un repertoire
			if( new File( sModel + File.separator + sScanDir ).isDirectory() ){
				
				// determine si le repertoire existe dans la destination
				if( !new File( sDest + File.separator + sScanDir ).exists() ) {
					FileUtils.forceMkdir( new File( sDest + File.separator + sScanDir ) );
				}
				
				// determine si celui-ci existe egalement dans la source
				if( new File( sSource + File.separator + sScanDir ).exists() ) {
					
					// merge le repertoire
					String SubSource = sSource + File.separator + sScanDir;
					String SubModel = sModel + File.separator + sScanDir;
					String SubDest = sDest + File.separator + sScanDir;
					this.mergeDirs( SubSource, SubModel, SubDest, oExtsTags );
				}
				continue;
			}
			
			// determine si le source n'existe pas
			if( !new File( sSource + File.separator + sScanDir ).exists() ){
				
				// copie le fichier du modele
				FileUtils.copyFile( new File( sModel + File.separator + sScanDir ), new File( sDest + File.separator + sScanDir ) );
			}else{
				// recupere l'extension du modele
				String sExtension = FilenameUtils.getExtension( sModel + File.separator + sScanDir ).toLowerCase().trim();
				if( !sExtension.equals( "" ) && oExtsTags.containsKey( sExtension ) ){
					// recupere les informations de fusion
					HashMap<String, String> oMergeInfos = (HashMap<String, String>)oExtsTags.get( sExtension );
					// recupere les informations des structures de la source et du modele
					HashMap<String, String> oStructSource = this.getStruct( sSource + File.separator + sScanDir, oMergeInfos );
					HashMap<String, String> oStructModel = this.getStruct( sModel + File.separator + sScanDir, oMergeInfos );
					// alimentation du fichier de model
					String sContentModel = new String( Files.readAllBytes( Paths.get( sModel + File.separator + sScanDir ) ) );
					for( String sSectionName : oStructModel.keySet() ) {
						if( !oStructSource.containsKey( sSectionName ) ) {
							continue;
						}
						// recherche de la section a alimenter
						Integer iPosBlock = sContentModel.indexOf( oMergeInfos.get("start") + sSectionName + oMergeInfos.get("start_end") );
						if( iPosBlock == -1 ){
							continue;
						}
						Integer iPosStopBlock = sContentModel.indexOf( oMergeInfos.get( "stop" ) + sSectionName, iPosBlock );
						if( iPosStopBlock == -1 ){
							continue;
						}
						// remplacement de la section
						sContentModel = sContentModel.substring( 0, iPosBlock )
								+ oMergeInfos.get( "start" ) + sSectionName + oMergeInfos.get( "start_end" )
								+ oStructSource.get( sSectionName )
								+ sContentModel.substring( iPosStopBlock );
					}
					// creation du nouveau fichier
					BufferedWriter bw = new BufferedWriter( new BufferedWriter( new FileWriter( new File( sDest + File.separator + sScanDir ) ) ) );
					bw.write( sContentModel );
					bw.close();

				// aucune information concernant le merge, copie du fichier du modele
				}else{
					FileUtils.copyFile( new File( sModel + File.separator + sScanDir ), new File( sDest + File.separator + sScanDir ) );
				}
			}

		// fin, foreach des fichiers / repertoires
		}
	}
}
