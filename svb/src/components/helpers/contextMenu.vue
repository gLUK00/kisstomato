<template>
	<div v-show="visible" class="ctxBackground">
		<div class="ctxContent" :style="'left: ' + this.position.x + 'px; top: ' + this.position.y + 'px'">
sdf4qsdf4 4qsd6f4qs6df4 qsd6f4qs56df4qs6df4qsd654f
4qsdf5qsd4fq q56sdf4 6qsd4fqs6d54fqs56d4fq6sd
		</div>
		
	<!-- more task items here... -->
	<!--</ul>
		<nav class="context-menu">
			<ul class="context-menu__items">
				<li class="context-menu__item">
					<a href="#" class="context-menu__link">
						<i class="fa fa-eye"></i> View Task
					</a>
				</li>
				<li class="context-menu__item">
					<a href="#" class="context-menu__link">
						<i class="fa fa-edit"></i> Edit Task
					</a>
				</li>
				<li class="context-menu__item">
					<a href="#" class="context-menu__link">
						<i class="fa fa-times"></i> Delete Task
					</a>
				</li>
			</ul>
		</nav>-->
	</div>
</template>

<script>
import Vue from 'vue'

export default {
	name: 'contextMenu',
	props: [ 'color' ],
	data() {
		return {
			visible: false,
			position: { x:0, y:0 }
			//renderComponent: 0
		}
	},
	computed: {

	},
	methods: {
		show( oItems, eSelect, position ) {
			this.visible = true
			this.position.x = position.x
			this.position.y = position.y

			//this.$log.info('this.color', this.color)
			console.log( 'ooooooooooooooooooooooooo' )
			console.log( this.visible )


			// determine la position de la sourie
			/*const { x, y } = useMousePosition();

			console.log( x + ' * ' + y );*/
			console.log( position.x + ' * ' + position.y )
		}
	}

}
</script>

<style scoped>
.ctxBackground{

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