<template>
	<div :ref-id="renderComponent">
		<div class="posNode" v-for="node in data" :key="getId(node)">
			<b-icon v-if="getChilds( node ).length == 0" class="posIcon" icon="octagon"></b-icon>
			<b-icon v-else-if="!asNodeOpen(node)" class="posIcon" icon="patch-plus" @click="eOpenClick( node )"></b-icon>
			<b-icon v-else-if="asNodeOpen(node)" class="posIcon" icon="patch-minus" @click="eOpenClick( node )"></b-icon>
			<span class="tagNode noselect" :style="'background-color:' + getColor( node )" @dblclick="eOpenClick( node )">{{ getName( node ) }}</span>
			<div v-if="asNodeOpen(node)" style="margin-left:15px">
				<treeNode :data="getChilds( node )" getIdMethode="getId" getChildsMethode="getChilds" getNameMethode="getName" getColorMethode="getColor"/>
			</div>
		</div>
	</div>
</template>

<script>
import treeNode from './treeNode'

const staticNodesOpen = {}

export default {
	name: 'treeNode',
	components: {
		treeNode
	},
	props: [ 'data', 'getIdMethode', 'getNameMethode', 'getChildsMethode', 'getColorMethode' ],
	computed: {

	},
	methods: {
		getId( node ){
			return this.$parent[ this.getIdMethode ]( node )
		},
		getName( node ){
			return this.$parent[ this.getNameMethode ]( node )
		},
		getChilds( node ){
			return this.$parent[ this.getChildsMethode ]( node )
		},
		getColor( node ){
			return this.$parent[ this.getColorMethode ]( node )
		},
		eOpenClick( node ){
			var sId = this.getId( node )
			this.nodesOpen[ sId ] = !this.asNodeOpen( node )
//console.log( 'eOpenClick : ' + sId + ' : ' + this.nodesOpen[ sId ] )
			this.forceRerender()
		},
		asNodeOpen( node ){
			if( this.getChilds( node ).length == 0 ){
				return false
			}
			var sId = this.getId( node )
			if( this.nodesOpen[ sId ] === undefined ){
				this.nodesOpen[ sId ] = false
			}
//console.log( 'asNodeOpen : ' + this.getName( node ) + ' : ' + sId + ' : ' + this.nodesOpen[ sId ] )
			return this.nodesOpen[ sId ]
		},
		forceRerender() {
			// Remove my-component from the DOM
			//this.renderComponent++

			this.$nextTick(() => {
				// Add the component back in
				this.renderComponent++
			});
		}
	},
	data(){
		return {
			nodesOpen: staticNodesOpen,
			renderComponent: 0
		}
	}
	//name: 'treeNode'
	/*props: [ 'keyId', 'keyName', 'keyChilds', 'keyColor' ],
	data() {
		return {
			colors: [ '4287f5', '3ff2e9', '3beb61', '55bd1e', 'e3e635', 'e39932', 'e35532', '5f31de', 'bd2fd6', 'd12ea0', 'c9284b' ]
		}
	},

octagon : rien
patch-minus : elements et ouvert
patch-plus : elements et ferme



	computed: {

	},
	methods: {
		select( item_color ) {
			this.$emit('update-color', item_color)
		},
		getClass( item_color ) {
			return this.color == item_color ? ' btn_color_selected' : ''
		}
	}*/


	//<treeNode :data="project.data" :getChilds="treeGetChilds" :getName="treeGetName" :getBgColor="treeGetBgColor"/>

}
</script>

<style scoped>
	.posNode{
		cursor: pointer;
	}
	.posIcon{
		float:left;
		width: 30px;
		margin-top: 10px;
	}
	.tagNode{
		border: 1px solid green;
		padding: 5px;
		border-radius: 5px;
		margin-bottom: 10px;
		display:flex;
		width: min-content;
	}
	.noselect {
		-webkit-touch-callout: none; /* iOS Safari */
		-webkit-user-select: none; /* Safari */
		-khtml-user-select: none; /* Konqueror HTML */
		-moz-user-select: none; /* Old versions of Firefox */
		-ms-user-select: none; /* Internet Explorer/Edge */
		user-select: none; /* Non-prefixed version, currently*/
	}
</style>