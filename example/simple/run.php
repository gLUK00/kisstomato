<?php
	include_once( '../../kisstomato.php' );
	define( 'PATH_BASE', dirname( __FILE__ ) );

	// rules of merge
	$oRulesMerge = array(
		'php'=>array( 'start'=>'// START-USER-', 'start_end'=>"\n", 'stop'=>'// STOP-USER-', 'stop_end'=>"\n" ),
		'js'=>array( 'start'=>'// START-USER-', 'start_end'=>"\n", 'stop'=>'// STOP-USER-', 'stop_end'=>"\n" ),

		// add for this example
		'txt'=>array( 'start'=>'# START-USER-', 'start_end'=>"\n", 'stop'=>'# STOP-USER-', 'stop_end'=>"\n" )
	);

	// create a model data
	$oModel = array( 'articles'=>array(
		array( 'id'=>1, 'title'=>'first article', 'content'=>'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.'),
		array( 'id'=>2, 'title'=>'second article', 'content'=>'Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.')
		),
	'title'=>'my first generation of text' );

	// get kisstomato helper
	$oKiss = kisstomato::get();

	// merge template with a model
	$oKiss->genFromTemplate( $oModel, PATH_BASE.'/temp_merge/articles.txt', PATH_BASE.'/templates/template.txt' );

	// merge from the production output
	$sPathProd = PATH_BASE.'/output_prod';
	$oKiss->mergeDirs( $sPathProd, PATH_BASE.'/temp_merge', $sPathProd, $oRulesMerge );