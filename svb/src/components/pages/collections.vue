<template>
	<div>
		<h1>Collections de l'application</h1>
		<div style="border:1px solid red;">
			<b-button variant="secondary" title="Supprimer le projet"><b-icon icon="arrow-left"></b-icon> Annuler</b-button>
			<b-button variant="success" title="Supprimer le projet"><b-icon icon="arrow-counterclockwise"></b-icon> Valider</b-button>
		</div>
		<div style="border:1px solid red;">
			<b-table striped hover :items="collections" caption-top>
				<template #cell(actions)="data">
					<b-button variant="success" title="Selectionner le projet"><b-icon icon="eye"></b-icon>{{ data.item.id }}</b-button>
					<b-button variant="danger" title="Supprimer le projet"><b-icon icon="trash2"></b-icon></b-button>
				</template>
			</b-table>
		</div>
		<div style="border:1px solid red;">
			<b-form>
				<b-form-group label="Nom de la collection :">
					<b-form-input
						v-model="collection.name"
						placeholder="Nom du projet"
						required/>
				</b-form-group>
				<b-form-group label="Description de la collection :">
					<b-form-input
						v-model="collection.description"
						placeholder="Enter name"
						required/>
				</b-form-group>
			</b-form>
			<b-table striped hover :items="collection.items" caption-top>
				<template #table-caption>Collections de bases</template>
				<template #cell(actions)="data">
		            <b-button variant="info"><b-icon icon="arrow-up"></b-icon></b-button>
		            <b-button variant="info"><b-icon icon="arrow-down"></b-icon></b-button>
		            <b-button variant="warning" title="Modifier l'élement" @click="updateItem"><b-icon icon="pencil-square"></b-icon></b-button>
		            <b-button variant="danger" title="Supprimer le projet"><b-icon icon="trash2"></b-icon></b-button>
		          </template>
			</b-table>
		</div>
		<b-modal id="modal-field" :title="'id : ' + item.id">
			<b-form>
				<b-form-group label="Nom de l'élément :">
					<b-form-input
						v-model="item.name"
						placeholder="Nom de l'élément"
						required/>
				</b-form-group>
				<b-form-group label="Description de l'élément :">
					<b-form-input
						v-model="item.description"
						placeholder="Description de l'élément"
						required/>
				</b-form-group>
			</b-form>
			<b-form inline>
    <label class="mr-sm-2" for="inline-form-custom-select-pref">Preference</label>
    <b-form-select
      id="inline-form-custom-select-pref"
      class="mb-2 mr-sm-2 mb-sm-0"
      :options="[{ text: 'Choose...', value: null }, 'One', 'Two', 'Three']"
      :value="null"
    ></b-form-select>

    <b-form-checkbox class="mb-2 mr-sm-2 mb-sm-0">Remember my preference</b-form-checkbox>

    <b-button variant="primary">Save</b-button>
  </b-form>
		</b-modal>
	</div>
</template>

<script>
export default {
	data() {
		return {
			collections: [
				{ root: 'oui', guid: '4sd54fd56s4g', name: 'page', description: 'liste des pages', actions: '' },
				{ root: '', guid: '6s5d4fg56sd4fg', name: 'component', description: 'liste des composants', actions: '' }
			],
			collection: { root: '', guid: '6s5d4fg56sd4fg', name: 'component', description: 'liste des composants', actions: '',
				items:[
					{ id: 'nssfsfsd', name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', cible: 'kiss:base_vars:integer', actions: '' },
					{ id: 'nssfsfsd', name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', cible: 'kiss:base_vars:integer', actions: '' },
					{ id: 'nssfsfsd', name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', cible: 'kiss:base_vars:integer', actions: '' },
					{ id: 'nssfsfsd', name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'object', cible: 'kiss:js:vuejs:v2', actions: '' }
				]
			},
			item: { id: 'nssfsfsd', name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', cible: 'kiss:base_vars:integer', actions: '' }
		}
	},
	methods: {
		updateItem() {
			this.$bvModal.show('modal-field')
		}
	}
}
</script>
