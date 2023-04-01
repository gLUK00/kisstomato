//$.jstree.defaults.core.themes.dir = "css/themes";
$('#tree').jstree({
	"core" : {
		'data' : [
       'Simple root node',
       {
         'text' : 'Root node 2',
         'icon': 'fa-solid fa-tree',
         'state' : {
           'opened' : true,
           'selected' : true
         },
         'children' : [
           { 'text' : 'Child 1' },
           'Child 2'
         ]
      }
    ]
	}
});