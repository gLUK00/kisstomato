<template>
	<div>
		<h1>Données du projet</h1>
		<b-row>
			<b-col cols="6" md="4">
				<!--<b-tree-view :data="treeData"></b-tree-view>-->
				<treeNode :data="treeData" keyId="guid" keyName="name" keyChilds="data" keyColor="color"/>
				<!-- https://github.com/kamil-lip/bootstrap-vue-treeview -->
			</b-col>
			<b-col cols="12" md="8">
				cccccccccccc
			</b-col>
		</b-row>
	</div>
</template>

<script>
import treeNode from '../helpers/treeNode'
//import { bTreeView } from 'bootstrap-vue-treeview'


//[ keyId="" keyName="" keyChilds="" keyColor=""]

export default {
	components: {
		/*bTreeView, treeNode*/
		treeNode
	},
	computed: {
		treeData(){
			
			// pour les noeuds racines
			var oNodes = []
			for( var i=0; i<this.project.collections.length; i++ ){
				if( this.project.collections[ i ].root ){
					var oCol = Object.assign( {}, this.project.collections[ i ] )

					// positionne les donnees de premier niveau associees a cette collection
					oCol.data = []
					for( var a=0; a<this.project.data.length; a++ ){
						if( this.project.data[ a ].guidCol == oCol.guid ){

							var oData = Object.assign( {}, this.project.data[ a ] )
							oData = this.preprareNode( oData )
							oCol.data.push( this.project.data[ a ] )
						}
					}

					oNodes.push( oCol )
				}
			}



			return [{"id": 2, "name": "Venus" , "children": [{"id": 3, "name": "Neptune"}, {"id": 4, "name": "Stratus"} ] }, {"id": 5, "name": "Uranus"} ]
		}
	},
	data() {
		return {
			//treeData: [{"id": 2, "name": "Venus" , "children": [{"id": 3, "name": "Neptune"}, {"id": 4, "name": "Stratus"} ] }, {"id": 5, "name": "Uranus"} ],
			project:{
				guid: '12s1fsd1fsdf',
				name: 'Project One',
				description: 'sqdfq qs dfqs dfsq dfsqdf qds fqsdfsqdfqdsfdsq',
				vars:[
					{ name: 'fsdfsdf', title: 'chaine', value: 'aaaaaaaa', type: 'string' },
					{ name: 'sdf', title: 'entier', value: 1234, type: 'integer' },
					{ name: 'ffff', title: 'float', value: 10.235, type: 'float' },
					{ name: 'a_cocher', title: 'case a cocher', value: true, type: 'boolean' },
					{ name: 'dddd', title: 'list', value: 'aaaaaaaa', type: 'list', items:['un', 'deux', 'trois'] }
				],
				collections: [
					{ guid: 'kiss:base_vars', description: 'Variable de bases' },
					{ guid: 'kiss:js:vuejs:v2', description: 'Vue JS v2' },
					{ color: '3ff2e9', root: true, guid: '4sd54fd56s4g-page', name: 'page', description: 'liste des pages',
						items:[
							{ guid: 'nssfsfsd', nodename: true, require: true, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer' },
							{ guid: 'nssfsfsd', require: false, name: 'component aa', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer' },
							{ guid: 'nssfsfsd', require: false, name: 'component bb', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer' },
							{ guid: 'nssfsfsd', require: true, name: 'component cc', description: 'dsf qsdfqs fsqdfqsd', type: 'object', target: 'kiss:js:vuejs:v2' }
						] },
					{ color: 'e3e635', root: false, guid: '6s5d4fg56sd4fg', name: 'component', description: 'liste des composants',
						items:[
							{ guid: 'nssfsfsd', require: true, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer' },
							{ guid: 'nssfsfsd', require: false, name: 'component aa', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer' },
							{ guid: 'nssfsfsd', require: false, name: 'component bb', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer' },
							{ guid: 'nssfsfsd', require: true, name: 'component cc', description: 'dsf qsdfqs fsqdfqsd', type: 'object', target: 'kiss:js:vuejs:v2' }
						] }
				],
				data:[
					{guid: "s65fs6d5fsd", guidCol: '4sd54fd56s4g-page',  data:[
						{ guid: '545s4-sdfsdf45s' }
					] }
				]
			}
		}
	},
	methods: {
		preprareNode( oData ){

			// recherche de la collection associees
			for( var i=0; i<this.project.collections.length; i++ ){
				if( this.project.collections[ i ].guid == oData.guidCol ){
					oData.color = this.project.collections[ i ].color
					break;
				}
			}
			//var oData = Object.assign( {}, this.data[ a ] )

			return oData
		}
	}
}
</script>

<style scoped>
	
</style>