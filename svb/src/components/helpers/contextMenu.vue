<template>
	<div>
		<ul class="tasks">
    <li class="task" data-id="3">
      <div class="task__content">
        Go To Grocery
      </div>
      <div class="task__actions">
        <i class="fa fa-eye"></i>
        <i class="fa fa-edit"></i>
        <i class="fa fa-times"></i>
      </div>
    </li>
    <!-- more task items here... -->
  </ul>
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
		</nav>
	</div>
</template>

<script>
export default {
	name: 'contextMenu',
	props: [ 'color' ],
	data() {
		return {
			//color: '3beb61',
			//mutableColor: this.color,
			colors: [ '4287f5', '3ff2e9', '3beb61', '55bd1e', 'e3e635', 'e39932', 'e35532', '5f31de', 'bd2fd6', 'd12ea0', 'c9284b' ]
		}
	},
	computed: {

	},
	methods: {
		show( oItems, eSelect ) {
			//this.$log.info('this.color', this.color)
			console.log( 'ooooooooooooooooooooooooo' )





		}
	}

}
</script>

<style scoped>
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
}
</style>