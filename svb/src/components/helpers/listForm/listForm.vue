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
				<!--<p class="p-3" @click="select(form)">Tab contents {{ form.id }}</p>
				<div>
					<template v-for="(field, iF) in form.fields">
						<template v-if="field.type == 'text'">
							<span>{{ field.name }}</span>

						</template>
						<span>{{ field.name }}</span> : <span>{{ field.type }}</span>
					</template>
				</div>-->
			</template>
		</b-tabs>
		<div v-if="activeForm != null">
			<template v-for="(field, iF) in activeForm.fields">
				<b-container fluid>
					<b-row class="row_form">
						<b-col sm="2">
							<label :for="field.id">{{ field.label }}</label>
						</b-col>
						<b-col sm="10">
							<template v-if="field.type == 'text'">
								<b-form-input :id="field.id" type="text" v-model="field.value"></b-form-input>
							</template>
							<template v-if="field.type == 'color'">
								<b-form-input :id="field.id" type="color" v-model="field.value"></b-form-input>
							</template>
							<template v-if="field.type == 'textarea'">
								<b-form-textarea :id="field.id" v-model="field.value" rows="3" max-rows="15"></b-form-textarea>
							</template>
							<template v-if="field.type == 'radio'">
								<b-form-group :label="field.label" v-slot="{ ariaDescribedby }">
									<b-form-radio v-for="(radio, indexRadio) in field.items" v-bind:key="field.id + indexRadio" v-model="field.value" :aria-describedby="ariaDescribedby" :name="field.id" :value="radio.value">&nbsp;{{ radio.label }}</b-form-radio>
								</b-form-group>
							</template>
							<template v-if="field.type == 'checkbox'">
								<b-form-group :label="field.label" v-slot="{ ariaDescribedby }">
									<b-form-checkbox-group v-for="(checkbox, indexCheckbox) in field.items" v-bind:key="field.id + indexCheckbox" v-model="field.values" :aria-describedby="ariaDescribedby" :name="field.id">
										<b-form-checkbox :value="checkbox.value">&nbsp;{{ checkbox.label }}</b-form-checkbox>
									</b-form-checkbox-group>
								</b-form-group>
							</template>
							<template v-if="field.type == 'list'">
								<span>Custom value : {{ field.value }}</span>
							</template>
							<!--<span>debug : {{ field.name }}</span> : <span>{{ field.type }}</span> : <span>{{ field.values }}</span> : <span>{{ field.value }}</span>-->
<!--
<label><input type="radio" v-model="item.type" value="list"/> Liste</label>
<label><input type="radio" v-model="item.type" value="object"/> Objet</label>
<label><input type="radio" v-model="item.type" value="objects"/> Collection d'objets</label>
-->
						</b-col>
					</b-row>
				</b-container>
			</template>
		</div>
	</div>
</template>

<script>
import listSelector from '../listSelector'

const oLstTypeFields = [ 'text', 'textarea', 'color', 'radio', 'checkbox', 'list', 'object', 'objects' ]

export default {
	//props: [ 'color' ],
	components: {
		listSelector
	},
	data() {
		return {
			//color: '3beb61',
			//mutableColor: this.color,
			activeForm: null,
			forms: this.devGetRandomForms(),
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

					var sTypeField = oLstTypeFields[ Math.floor(Math.random() * oLstTypeFields.length) ]
					/*while( sTypeField == 'custom' ){
						sTypeField = oLstTypeFields[ Math.floor(Math.random() * oLstTypeFields.length) ]
					}*/
					var oField = { type: sTypeField, id: 'field_' + ( Date.now() + ( Math.random() * 1000 ) ), label: 'field ' + sTypeField + ' ' + iField }
					if( sTypeField == 'text' || sTypeField == 'custom' ){
						oField.value = (Math.random() + 1).toString(36).substring(7)
					}else if( sTypeField == 'textarea' ){
						oField.value = (Math.random() + 1).toString(36)
					}else if( sTypeField == 'color' ){
						oField.value = Math.floor(Math.random()*16777215).toString(16)
					}else if( sTypeField == 'radio' ){
						oField.items = []
						oField.value = null
						var iNbrRadios = Math.floor(Math.random() * 10) + 1
						for( var iRadio = 0; iRadio < iNbrRadios; iRadio++ ){
							oField.items.push( { value: ( Date.now() + ( Math.random() * 1000 ) ), label: 'label radio ' + Math.floor(Math.random()*16777215).toString(16) } )
						}

						// determine si il y a une selection
						if( Math.random() > 0.5 && oField.items.length > 0 ){

							// selectionne un radio
							oField.value = oField.items[ Math.floor(Math.random() * oField.items.length) ].value
						}
					}else if( sTypeField == 'checkbox' ){
						oField.items = []
						oField.values = []
						var iNbrCheckbox = Math.floor(Math.random() * 10) + 1
						for( var icheck = 0; icheck < iNbrCheckbox; icheck++ ){
							oField.items.push( { value: ( Date.now() + ( Math.random() * 1000 ) ), label: 'label checkbox ' + Math.floor(Math.random()*16777215).toString(16) } )

							// determine si il y a selection
							if( Math.random() > 0.5 && oField.items.length > 0 ){

								// selectionne un radio
								oField.values.push( oField.items[ oField.items.length - 1 ].value )
							}
						}
					}else if( sTypeField == 'list' || sTypeField == 'object' || sTypeField == 'objects' ){

					}
					
					oForm.fields.push( oField )
				}


				oForms.push( oForm )
			}

			// selection asynchrone du premier formulaire
			if( oForms.length > 0 && this.activeForm == null ){
				this.$nextTick(() => {
					this.select( oForms[ 0 ] )
				});
			}

			return oForms
		}
	}

}
</script>

<style scoped>
	.row_form{
		margin-bottom: 5px;
	}
</style>