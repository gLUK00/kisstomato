<template>
	<div>
		<div class="posNode" v-for="node in data">
			<span class="tagNode" :style="'background-color:' + getColor( node )">{{ getName( node ) }}</span>
			<div v-if="getChilds( node ).length > 0" style="margin-left:15px">
				<treeNode :data="getChilds( node )" getChildsMethode="getChilds" getNameMethode="getName" getColorMethode="getColor"/>
			</div>
		</div>
	</div>
</template>

<script>
import treeNode from './treeNode'

export default {
	name: 'treeNode',
	components: {
		treeNode
	},
	props: [ 'data', 'getNameMethode', 'getChildsMethode', 'getColorMethode' ],
	methods: {
		getName( node ){
			return this.$parent[ this.getNameMethode ]( node )
		},
		getChilds( node ){
			return this.$parent[ this.getChildsMethode ]( node )
		},
		getColor( node ){
			return this.$parent[ this.getColorMethode ]( node )
		}
	}
	//name: 'treeNode'
	/*props: [ 'keyId', 'keyName', 'keyChilds', 'keyColor' ],
	data() {
		return {
			colors: [ '4287f5', '3ff2e9', '3beb61', '55bd1e', 'e3e635', 'e39932', 'e35532', '5f31de', 'bd2fd6', 'd12ea0', 'c9284b' ]
		}
	},
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
		width: min-content;
	}
	.tagNode{
		border: 1px solid green;
		padding: 5px;
		border-radius: 5px;
		margin-bottom: 10px;
		display:block;
	}
</style>