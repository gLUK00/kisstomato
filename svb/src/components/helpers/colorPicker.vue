<template>
	<div>
		<span>Couleur :</span>
		<div style="padding: 5px 10px;">
			<div v-for="item_color in colors" :key="item_color" :class="[ 'btn_color', getClass( item_color ) ]" :style="'background-color: #' + item_color" @click="select(item_color)">&nbsp;</div>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			color: '3beb61',
			colors: [ '4287f5', '3ff2e9', '3beb61', '55bd1e', 'e3e635', 'e39932', 'e35532', '5f31de', 'bd2fd6', 'd12ea0', 'c9284b' ]
		}
	},
	computed: {

	},
	methods: {
		select( item_color ) {
			//this.$log.info('this.color', this.color)
			this.color = item_color
		},
		getClass( item_color ) {
			return this.color == item_color ? ' btn_color_selected' : ''
		}
	}

}
</script>

<style scoped>
	.btn_color{
		width: 40px;
		margin-right: 10px;
		float: left;
		border-radius: 5px;
		cursor: pointer;
	}
	.btn_color:hover{
		outline: 3px solid DodgerBlue;
		outline-offset: 4px
	}
	.btn_color_selected{
		outline: 3px solid ForestGreen;
		outline-offset: 4px
	}
</style>