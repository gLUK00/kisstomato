<template>
	<div>
		<b-tabs content-class="mt-3">
			<template v-for="(form, index) in forms">
				<b-tab v-if="(activeForm != null && form.id == activeForm.id) || (activeForm == null && index == 0)" active>
					<template #title>
						<b-icon icon="x-circle"></b-icon> {{form.name}}
						<span v-if="form.state == 'edit'">&nbsp;*</span>
					</template>
					<p class="p-3" @click="select(form)">Tab contents {{ form.id }}</p>
				</b-tab>
				<b-tab v-else @click="select(form)">
					<template #title>
						{{form.name}}
						<span v-if="form.state == 'edit'">&nbsp;*</span>
					</template>
					<p>I'm the second tab {{ form.id }}</p>
				</b-tab>
			</template>
			<!--<b-tab active>
				<template #title>
					<b-icon icon="x-circle"></b-icon> First
				</template>
				<p class="p-3">Tab contents 1</p>
			</b-tab>
			<b-tab title="Second"><p>I'm the second tab</p></b-tab>
			<b-tab title="bbbbb"><p>I'm a disabled tab!</p></b-tab>-->
		</b-tabs>
	</div>
</template>

<script>
export default {
	//props: [ 'color' ],
	data() {
		return {
			//color: '3beb61',
			//mutableColor: this.color,
			activeForm: null,
			forms: [
				{ id: '12121', name: 'Conversion', state: 'view', fields: [
					{ id: '5454', type:'text', value: 'sdfsfsdf'},
					{ id: '54541', type:'textarea', value: 'aaaaaaaaa'},
					{ id: '54542', type:'radio', options: [ {id: '11', label: 'eee'}, {id: '12', label: 'fff'} ], value: '12' }
					]
				},
				{ id: '12', name: 'Redimension', state: 'view', active: true, fields: [
					{ id: '5454', type:'text', value: 'sdfsfsdf'},
					{ id: '54541', type:'textarea', value: 'aaaaaaaaa'},
					{ id: '54542', type:'radio', options: [ {id: '11', label: 'eee'}, {id: '12', label: 'fff'} ], value: '12' }
					]
				},
				{ id: '13', name: 'Adaptateur', state: 'edit', fields: [
					{ id: '5454', type:'text', value: 'sdfsfsdf'},
					{ id: '54541', type:'textarea', value: 'aaaaaaaaa'},
					{ id: '54542', type:'radio', options: [ {id: '11', label: 'eee'}, {id: '12', label: 'fff'} ], value: '12' }
					]
				}
			]
		}
	},
	computed: {

	},
	methods: {
		select( oForm ){
			this.activeForm = oForm
			console.log( this.activeForm.id )
		}
	}

}
</script>

<style scoped>
	
</style>