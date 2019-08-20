# KISSTOMATO

A code generator engine in PHP/JAVA for all.

## Operating principle

![](https://gluk00.github.io/ehidalgo.github.io/assets/images/kisstomato_principe.png)

## Example code in PHP :

```
<?php

// include a helper class
include_once( 'kisstomato.php' );

// define your rules of merge
$oRulesMerge = array(
	'php'=>array( 'start'=>'// START-USER-', 'start_end'=>PHP_EOL, 'stop'=>'// STOP-USER-', 'stop_end'=>PHP_EOL ),
	'js'=>array( 'start'=>'// START-USER-', 'start_end'=>PHP_EOL, 'stop'=>'// STOP-USER-', 'stop_end'=>PHP_EOL ),
	'txt'=>array( 'start'=>'# START-USER-', 'start_end'=>PHP_EOL, 'stop'=>'# STOP-USER-', 'stop_end'=>PHP_EOL )
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

## Example code in JAVA :

```
HashMap<String, HashMap<String, String>> oExtsTags = new HashMap<String, HashMap<String,String>>();

HashMap<String, String> oRulesJS = new HashMap<String, String>();
oRulesJS.put("start", "// START-USER-");
oRulesJS.put("start_end", "\r\n");
oRulesJS.put("stop", "// STOP-USER-");
oRulesJS.put("stop_end", "\r\n");
oExtsTags.put("js", oRulesJS);

HashMap<String, String> oRulesHTML = new HashMap<String, String>();
oRulesHTML.put("start", "<!-- START-USER-");
oRulesHTML.put("start_end", "-->\r\n");
oRulesHTML.put("stop", "<!-- STOP-USER-");
oRulesHTML.put("stop_end", "-->\r\n");
oExtsTags.put("html", oRulesHTML);

Kisstomato.getInstance().mergeDirs(dirCible, tempDir, dirCible, oExtsTags);
```
