<template>
	<div v-on:mousemove="ctxMenuPosition">
		<h1>Données du projet</h1>
		<b-row>
			<b-col cols="6" md="4">
				<!--<treeNode :data="treeData" keyId="guid" keyName="name" keyChilds="data" keyColor="color"/>-->
				<!--<treeNode :data="project.data" getIdMethode="treeGetId" getChildsMethode="treeGetChilds" getNameMethode="treeGetName" getColorMethode="treeGetBgColor"/>-->
				<treeNode :data="treeData" getIdMethode="treeGetId" getChildsMethode="treeGetChilds" getNameMethode="treeGetName" getColorMethode="treeGetBgColor" rightClick="treeRightClick" dblclick="treeDblclick"/>
				<!-- https://github.com/kamil-lip/bootstrap-vue-treeview -->
			</b-col>
			<b-col cols="12" md="8">
				cccccccccccc
			</b-col>
		</b-row>
		<contextMenu ref="componentContextMenu" selectItem="selectContextItem"/>
	</div>
</template>

<script>
import treeNode from '../helpers/treeNode'
import contextMenu from '../helpers/contextMenu'

export default {
	components: {
		treeNode,
		contextMenu
	},
	computed: {
		treeData(){
			
			// pour les noeuds racines
			var oNodes = []
			for( var i=0; i<this.project.collections.length; i++ ){
				if( this.project.collections[ i ].root ){
					var oCol = Object.assign( {}, this.project.collections[ i ] )
					oCol.__asRootCol = true

					// positionne les donnees de premier niveau associees a cette collection
					oCol.childs = []
					for( var a=0; a<this.project.data.length; a++ ){
						if( this.project.data[ a ].guidCol == oCol.guid ){
							var oData = Object.assign( {}, this.project.data[ a ] )
							oCol.childs.push( this.project.data[ a ] )
						}
					}

					oNodes.push( oCol )
				}
			}

			return oNodes
		}
	},
	data() {
		return {
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
					{ guid: "auth-s65fs6d5fsd", guidCol: '4sd54fd56s4g-page', data: [
						{ guid: 'anssfsfsd1', guidItem: 'nssfsfsd1', value: 'authentification' },
						{ guid: 'anssfsfsd2', guidItem: 'nssfsfsd2', value: 'page d\'authentification' },
						{ guid: 'anssfsfsd3', guidItem: 'nssfsfsd3', value: false }
					], childs:[
						{ guid: 'message-1sf1sd2f1d1', guidCol: '6s5d4fg56sd4fg', data: [
							{ guid: 'g4hj56g4hj4', guidItem: 'nssfsfsd0', value: 'message' },
							{ guid: 'g4hj56g4hj4e', guidItem: 'nssfsfsd1', value: 'bienvenu sur la page d\'authentification' }
						] }
					] },
					{ guid: '65d46d5fg', guidCol: '6s5d4fg56sd4fg1', data: [
						{ guid: 'sdf444', guidItem: 'nssfsfsd4', value: 'colorPicker' },
						{ guid: 'sdf445', guidItem: 'nssfsfsd5', value: [ 'color' ] }
					] }
				]
			},
			position: { x:0, y:0 }
		}
	},
	methods: {
		treeGetChilds( oNode ){
			if( oNode.childs ){
				return oNode.childs
			}
			return []
		},
		treeGetId( oNode ){
			return oNode.guid
		},
		treeGetName( oNode ){
			if( oNode.__asRootCol ){
				return oNode.name
			}

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
			if( oNode.__asRootCol ){
				return '#' + oNode.color
			}

			// recherche de la collection associee
			var oCol = this.getColByGuid( oNode.guidCol )
			//console.log( '#' + oCol.color )
			return '#' + oCol.color
		},
		treeDblclick( oNode ){

console.log( 'ouverture' )
console.log( oNode )

		},

		// alimentate la position du menu contextuel
		ctxMenuPosition( event ){
			this.position.x = event.clientX;
			this.position.y = event.clientY;
		},

		// evenement de click droit sur un element du treeview
		treeRightClick( node ){
console.log( 'treeRightClick : ' + node.guid )

			this.$refs.componentContextMenu.show( [
					{ text: 'Menu 1', id: 12, color:'3ff2e9' },
					{ text: 'Menu 2', id: 13, color:'ccc' },
					{ type: 'separator' },
					{ text: 'Menu 3', id: 14, color:'3ff2e9', disabled: true },
					{ text: 'Menu 4', id: 15, color:'e3e635' }
				], this.selectContextItem, this.position )

//contextMenu.show( [], this.xxxxxxxxxx )

		},

		// selection d'un element du menu contextuel
		selectContextItem( item ){

console.log( 'selectContextItem >>' )
console.log( item.id )

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

	}
}
</script>

<style scoped>
	
</style>