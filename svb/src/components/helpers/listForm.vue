<template>
	<div>
		<b-tabs content-class="mt-3">
			<template v-for="(form, index) in forms">
				<b-tab v-if="(activeForm != null && form.id == activeForm.id) || (activeForm == null && index == 0)" active>
					<template #title>
						<b-icon icon="x-circle"></b-icon> {{form.name}}
						<span v-if="form.state == 'edit'">&nbsp;*</span>
					</template>
				</b-tab>
				<b-tab v-else @click="select(form)">
					<template #title>
						{{form.name}}
						<span v-if="form.state == 'edit'">&nbsp;*</span>
					</template>
				</b-tab>
				<p class="p-3" @click="select(form)">Tab contents {{ form.id }}</p>
				<div>
					<template v-for="(field, iF) in form.fields">
						<span>{{ field.name }}</span> : <span>{{ field.value }}</span>
					</template>
				</div>
			</template>
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
			forms: this.devGetRandomForms()
			/*forms: [
				{ id: '12121', name: 'Conversion', state: 'view', fields: [
					{ id: '5454', type:'text', name:"aaa", value: 'sdfsfsdf'},
					{ id: '54541', type:'textarea', name:"aaa", value: 'aaaaaaaaa'},
					{ id: '54542', type:'radio', name:"aaa", options: [ {id: '11', label: 'eee'}, {id: '12', label: 'fff'} ], value: '12' }
					]
				},
				{ id: '12', name: 'Redimension', state: 'view', active: true, fields: [
					{ id: '5454', type:'text', name:"aaa", value: 'sdfsfsdf'},
					{ id: '54541', type:'textarea', name:"aaa", value: 'aaaaaaaaa'},
					{ id: '54542', type:'radio', name:"aaa", options: [ {id: '11', label: 'eee'}, {id: '12', label: 'fff'} ], value: '12' }
					]
				},
				{ id: '13', name: 'Adaptateur', state: 'edit', fields: [
					{ id: '5454', type:'text', name:"aaa", value: 'sdfsfsdf'},
					{ id: '54541', type:'textarea', name:"aaa", value: 'aaaaaaaaa'},
					{ id: '54542', type:'radio', name:"aaa", options: [ {id: '11', label: 'eee'}, {id: '12', label: 'fff'} ], value: '12' }
					]
				}
			]*/
		}
	},
	computed: {
		//this.forms = this.devGetRandomForms()
	},
	methods: {
		select( oForm ){
			this.activeForm = oForm
			console.log( this.activeForm.id )
		},
		devGetRandomForms(){
			var oForms = []
			var oRandListNames = [ 'Roseanna', 'Swilley', 'Pat', 'Parkison', 'Lavern', 'Ikard', 'Diamond', 'Pizzuto', 'Rima', 'Wimberly', 'Asia', 'Vanhoy', 'Lucilla', 'Poor', 'Theresa', 'Mastropietro', 'Candie', 'Figueras', 'Alta', 'Lonergan', 'Danyelle', 'Demille', 'Susannah', 'Frasure', 'Robert', 'Mani', 'Deadra', 'Losada', 'Claudette', 'Dyck', 'Florentino', 'Stalnaker', 'Margareta', 'Beaufort', 'Alana', 'Beringer', 'Bettyann', 'Homeyer', 'Monserrate', 'Carranza' ]
			var iNbrForms = Math.floor(Math.random() * 10)
			for( var iForm = 0; iForm < iNbrForms; iForm++ ){
				var oForm = {id: 'form_' + iForm, name: oRandListNames[ Math.floor(Math.random() * oRandListNames.length) ], state: Math.random() > 0.5 ? 'edit' : 'view', fields: [] }

				var iNbrFields = Math.floor(Math.random() * 10)
				for( var iField = 0; iField < iNbrFields; iField++ ){

				}


				oForms.push( oForm )
			}

			return oForms
		}
	}

}
</script>

<style scoped>
	
</style>