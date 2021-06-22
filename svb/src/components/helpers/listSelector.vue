<template>
	<div>
		<span class="message tagColor" v-if="keyInItems" :style="'background-color:#' + target[ keyColor ] + ';'">{{ target[ keyName ] }}</span>
		<span class="message" v-else>Aucune selection</span>
		<b-button variant="info" @click="showList"><b-icon icon="arrow-up"></b-icon></b-button>
		<b-modal id="modal-select-one" :title="title">
			<b-list-group>
				<b-list-group-item button v-for="item in items" :key="item[ keyId ]" :style="'background-color:#' + item[ keyColor ] + ';'" @click="selectElement(item)">{{ item[ keyName ] }}</b-list-group-item>
			</b-list-group>
		</b-modal>
	</div>
</template>

<script>
export default {
	props: [ 'title', 'items', 'target', 'keyId', 'keyName', 'keyColor' ],
	data() {
		return {
			//color: '3beb61',
			//mutableColor: this.color,
			colors: [ '4287f5', '3ff2e9', '3beb61', '55bd1e', 'e3e635', 'e39932', 'e35532', '5f31de', 'bd2fd6', 'd12ea0', 'c9284b' ]
		}
	},
	computed: {
		keyInItems(){
			if( this.target != null && this.target[ this.keyName ] === undefined ){
				return false
			}
			for( var i=0; i<this.items.length; i++ ){
				if( this.items[ i ] ==  this.target ){
					return true
				}
			}
			return false
		}
	},
	methods: {
		showList() {
			this.$bvModal.show('modal-select-one')
		},
		selectElement( selectItem ) {
			this.$emit('select-item', selectItem)
			this.$bvModal.hide('modal-select-one')
			//this.$bvModal.show('modal-select-one')
		}
	}

}
</script>

<style scoped>
	.message{
		margin-right:5px;
	}
	.tagColor{
		padding: 3px 5px;
		border-radius: 7px;
	}
</style>