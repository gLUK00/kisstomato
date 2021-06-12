<template>
	<div>
		<b-button variant="primary"><b-icon icon="plus-circle"></b-icon> Modifier le projet</b-button>
		<b-form v-if="show">
			<b-form-group label="Nom du projet :">
				<b-form-input
					v-model="project.name"
					placeholder="Nom du projet"
					required/>
			</b-form-group>
			<b-form-group label="Description du projet :">
				<b-form-input
					v-model="project.description"
					placeholder="Enter name"
					required/>
			</b-form-group>
			<b-table striped hover :items="project.collections" caption-top>
				<template #table-caption>Collections de bases</template>
			</b-table>
		</b-form>
	</div>
</template>

<script>
export default {
	data() {
		return {
			project: {
				name: 'Project one',
				description: 'sqdfq qs dfqs dfsq dfsqdf qds fqsdfsqdfqdsfdsq',
				collections: [
					{ guid: 'kiss:base_vars', description: 'Variable de bases' },
					{ guid: 'kiss:js:vuejs:v2', description: 'Vue JS v2' }
				]
			},
			show: true
		}
	}
}
</script>
