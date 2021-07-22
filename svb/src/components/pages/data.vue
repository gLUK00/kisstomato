<template>
	<div>
		<h1>Données du projet</h1>
		<b-row>
			<b-col cols="6" md="4">
				<!--<treeNode :data="treeData" keyId="guid" keyName="name" keyChilds="data" keyColor="color"/>-->
				<treeNode :data="project.data" getChildsMethode="treeGetChilds" getNameMethode="treeGetName" getColorMethode="treeGetBgColor"/>
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
		/*treeData(){
			
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
		}*/
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
							{ guid: 'nssfsfsd1', nodename: true, require: true, name: 'nom', description: 'nom de la page', type: 'variable', target: 'kiss:base_vars:string' },
							{ guid: 'nssfsfsd2', require: false, name: 'fonction', description: 'fonction la page', type: 'variable', target: 'kiss:base_vars:integer' },
							{ guid: 'nssfsfsd3', require: false, name: 'secure', description: '', type: 'page securisée', target: 'kiss:base_vars:boolean', default: false },
							{ guid: 'nssfsfsd4', require: true, name: 'component cc', description: 'dsf qsdfqs fsqdfqsd', type: 'object', target: 'kiss:js:vuejs:v2' }
						] },
					{ color: 'e3e635', root: true, guid: '6s5d4fg56sd4fg', name: 'zone_de_contenu', description: 'zones de contenus',
						items:[
							{ guid: 'nssfsfsd0', nodename: true, require: true, name: 'nom', description: 'nom de la zone', type: 'variable', target: 'kiss:base_vars:string' },
							{ guid: 'nssfsfsd1', require: true, name: 'contenu', description: 'contenu de la zone', type: 'variable', target: 'kiss:base_vars:string' }
						] },
					{ color: 'e3e635', root: true, guid: '6s5d4fg56sd4fg1', name: 'component', description: 'liste des composants',
						items:[
							{ guid: 'nssfsfsd4', nodename: true, require: true, name: 'nom', description: 'nom du composant', type: 'variable', target: 'kiss:base_vars:string' },
							{ guid: 'nssfsfsd5', require: false, name: 'props', description: 'proprietes', type: 'variable', target: 'kiss:base_vars:list' }
						] }
				],
				data:[
					{ guid: "s65fs6d5fsd", guidCol: '4sd54fd56s4g-page', data: [
						{ guid: 'anssfsfsd1', guidItem: 'nssfsfsd1', value: 'authentification' },
						{ guid: 'anssfsfsd2', guidItem: 'nssfsfsd2', value: 'page d\'authentification' },
						{ guid: 'anssfsfsd3', guidItem: 'nssfsfsd3', value: false }
					], childs:[
						{ guid: '1sf1sd2f1d1', guidCol: '6s5d4fg56sd4fg', data: [
							{ guid: 'g4hj56g4hj4', guidItem: 'nssfsfsd0', value: 'message' },
							{ guid: 'g4hj56g4hj4e', guidItem: 'nssfsfsd1', value: 'bienvenu sur la page d\'authentification' }
						] }
					] },
					{ guid: '65d46d5fg', guidCol: '6s5d4fg56sd4fg1', data: [
						{ guid: 'sdf444', guidItem: 'nssfsfsd4', value: 'colorPicker' },
						{ guid: 'sdf445', guidItem: 'nssfsfsd5', value: [ 'color' ] }
					] }
				]
			}
		}
	},
	methods: {
		treeGetChilds( oNode ){
			if( oNode.childs ){


console.log( 'yyyyyyyyyyyyyyyy' )

				return oNode.childs
			}
			return []
		},
		treeGetName( oNode ){
			var sName = ''

			// recherche de la collection associee
			var oCol = this.getColByGuid( oNode.guidCol )

			// recherche le "nodename"
			for( var i=0; i<oCol.items.length; i++ ){
				if( oCol.items[ i ].nodename ){
					var oData = this.getObjDataByGuidItem( oNode, oCol.items[ i ].guid )
					if( sName != '' ){
						sName += ' '
					}
					sName += oData.value
				}
			}

			return sName
		},
		treeGetBgColor( oNode ){

			// recherche de la collection associee
			var oCol = this.getColByGuid( oNode.guidCol )
			console.log( '#' + oCol.color )
			return '#' + oCol.color
		},

		// les collections
		
		getColByGuid( sGuid ){
			for( var i=0; i<this.project.collections.length; i++ ){
				if( this.project.collections[ i ].guid == sGuid ){
					return this.project.collections[ i ]
				}
			}
			return null
		},

		// les objets

		getObjDataByGuidItem( oNode, sGuidItem ){
			
			for( var i=0; i<oNode.data.length; i++ ){
				if( oNode.data[ i ].guidItem == sGuidItem ){
					return oNode.data[ i ]
				}
			}

			return null
		}

		/*,
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
		}*/
	}
}
</script>

<style scoped>
	
</style>