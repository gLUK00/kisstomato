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
				<b-form-checkbox><span class="chk">Utiliser ce champ comme nom du noeud</span></b-form-checkbox>
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
				<b-form-group label="Description de l'élément :">
					<b-form-radio-group v-model="item.type" inline="true">
						<b-form-radio value="variable">Variable</b-form-radio>
						<b-form-radio value="object">Objet</b-form-radio>
					</b-form-radio-group>
				</b-form-group>
			</b-form>
			<b-form inline>
				<b-form-checkbox-group>
					<b-form-checkbox><span class="chk">Variable</span></b-form-checkbox>
					<b-form-checkbox><span class="chk">Objet</span></b-form-checkbox>
				</b-form-checkbox-group>
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

<style scoped>
	.chk{
		padding-left: 10px;
	}
</style>