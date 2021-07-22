<template>
	<div>
		<div class="node" v-for="node in data">
			<span>{{ getName( node ) }}</span>
		</div>


		zzz
		<div>
nnn
			<div>
ddddddddd ddddddddddddddddddddddddddddddd
			</div>
		</div>
	</div>
</template>

<script>
export default {
	props: [ 'data', 'getNameMethode' ],
	methods: {
		getName( node ){

			//console.log( this.$emit('getName', node) )
			//console.log( this.getNameMethode )
			//console.log( this.$parent[ this.getNameMethode ]( node ) )
			return this.$parent[ this.getNameMethode ]( node )
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
	.node{
		border: 1px solid red;
		width: 300px;
	}
</style>