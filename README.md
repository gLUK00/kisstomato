# KISSTOMATO

A code generator engine in PHP for all.

## Operating principle

![](https://gluk00.github.io/ehidalgo.github.io/assets/images/kisstomato_principe.png)

## Example code :

```
<?php

// include a helper class
include_once( 'kisstomato.php' );

// define your rules of merge
$oRulesMerge = array(
	'php'=>array( 'start'=>'// START-USER-', 'start_end'=>"\n", 'stop'=>'// STOP-USER-', 'stop_end'=>"\n" ),
	'js'=>array( 'start'=>'// START-USER-', 'start_end'=>"\n", 'stop'=>'// STOP-USER-', 'stop_end'=>"\n" ),
	'txt'=>array( 'start'=>'# START-USER-', 'start_end'=>"\n", 'stop'=>'# STOP-USER-', 'stop_end'=>"\n" )
);

// create a data model
$oModel = array( 'key'=>'value' );

// get kisstomato helper
$oKiss = kisstomato::get();

// merge template with a model
$oKiss->genFromTemplate( $oModel, 'file temp to merge', 'file to template' );

// merge from the production output
$oKiss->mergeDirs( 'your path of reference, or path to output', 'your path temp merge', 'your path to output', $oRulesMerge );

```

