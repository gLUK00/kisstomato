<template>
	<div v-show="visible" class="ctxBackground" @click="hide" @contextmenu="hide">
		<div class="ctxContent" :style="'left: ' + this.position.x + 'px; top: ' + this.position.y + 'px'">
			<b-list-group>
				<template v-for="(item, index) in items">
					<b-list-group-item v-if="item.type && item.type=='separator'" @click.stop="select(item)">&nbsp;</b-list-group-item>
					<b-list-group-item v-else button :style="'background-color:#' + item.color" @click.stop="select(item)">
						<span v-if="item.disabled" style="color: rgba(255, 255, 255, 0.8)">{{ item.text }}</span>
						<span v-else>{{ item.text }}</span>
					</b-list-group-item>
				</template>
			</b-list-group>
		</div>
	</div>
</template>

<script>
import Vue from 'vue'

export default {
	name: 'contextMenu',
	props: [ 'selectItem' ],
	data() {
		return {
			visible: false,
			position: { x:0, y:0 },
			items: []
			//renderComponent: 0
		}
	},
	computed: {

	},
	methods: {
		hide( e ){
			this.visible = false
			e.preventDefault()
		},
		show( oItems, eSelect, position ) {
			this.visible = true
			this.position.x = position.x
			this.position.y = position.y
			this.items = oItems
		},
		select( item ){
			if( ( item.type !== undefined && item.type == 'separator' ) ||
				( item.disabled !== undefined && item.disabled == true ) ){
				return
			}

			// masque l'affichage
			this.visible = false

			// propagation de l'evenement
			if( this.$parent[ this.selectItem ] === undefined ){
				return
			}
			this.$parent[ this.selectItem ]( item )
		}
	}

}
</script>

<style scoped>
.ctxBackground{
	/*background-color: red;*/

	min-height: 100%;
	min-width: 1024px;

	/* Set up proportionate scaling */
	width: 100%;
	height: auto;

	/* Set up positioning */
	position: fixed;
	top: 0;
	left: 0;

}
.ctxContent{
	position: fixed;
	border: 1px solid red;
}
/*
.tasks {
	list-style: none;
	margin: 0;
	padding: 0;
}

.task {
	display: flex;
	justify-content: space-between;
	padding: 12px 0;
	border-bottom: solid 1px #dfdfdf;
}

.task:last-child {
	border-bottom: none;
}

.context-menu {
	display: none;
	position: absolute;
	z-index: 10;
}

.context-menu--active {
	display: block;
}*/
</style>