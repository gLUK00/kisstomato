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
				<b-form-group class="element" label="Nom de la collection :">
					<b-form-input
						v-model="collection.name"
						placeholder="Nom du projet"
						required/>
				</b-form-group>
				<b-form-group class="element" label="Description de la collection :">
					<b-form-input
						v-model="collection.description"
						placeholder="Enter name"
						required/>
				</b-form-group>
			</b-form>
			<colorPicker/>
			<b-table striped hover :items="collection.items" caption-top>
				<template #table-caption>Element de la collections</template>
				<template #cell(actions)="data">
		            <b-button variant="info"><b-icon icon="arrow-up"></b-icon></b-button>
		            <b-button variant="info"><b-icon icon="arrow-down"></b-icon></b-button>
		            <b-button variant="warning" title="Modifier l'élement" @click="updateItem"><b-icon icon="pencil-square"></b-icon></b-button>
		            <b-button variant="danger" title="Supprimer le projet"><b-icon icon="trash2"></b-icon></b-button>
		          </template>
		          <template #cell(require)="data">
		          	<span v-if="data.item.require">Oui</span>
		          </template>
			</b-table>
			<b-button variant="success" title="Ajouter un élément"><b-icon icon="plus-circle"></b-icon> Ajouter un élément</b-button>
		</div>
		<b-modal id="modal-field" :title="'id : ' + item.id">
			<b-form>
				<b-form-checkbox class="element"><span class="chk">Utiliser ce champ comme nom du noeud</span></b-form-checkbox>
				<b-form-checkbox class="element"><span class="chk">Rendre sa saisie obligatoire</span></b-form-checkbox>
				<b-form-group class="element" label="Nom de l'élément :">
					<b-form-input
						v-model="item.name"
						placeholder="Nom de l'élément"
						required/>
				</b-form-group>
				<b-form-group class="element" label="Description de l'élément :">
					<b-form-input
						v-model="item.description"
						placeholder="Description de l'élément"
						required/>
				</b-form-group>
				<div class="element">
					<span>Type d'élément :</span>
					<label><input type="radio" v-model="item.type" value="variable"/> Variable</label>
					<label><input type="radio" v-model="item.type" value="object"/> Objet</label>
					<label><input type="radio" v-model="item.type" value="objects"/> Collection d'objets</label>
				</div>
				<b-form-group v-if="item.type == 'variable'" class="element" label="Type de variable :">
					<b-form-select v-model="item.target" :options="type_de_vars"></b-form-select>
				</b-form-group>
				<div v-if="item.type != 'variable'">
					<span>Objet séléctionné :</span>
					<div>
						<span>Le nom de l'objet</span>
						<b-button variant="info" @click="selectElement"><b-icon icon="arrow-up"></b-icon></b-button>
					</div>
				</div>
			</b-form>
		</b-modal>
		<b-modal id="modal-select-one" :title="'id : ' + item.id">
			<b-list-group>
				<b-list-group-item button variant="danger">Button item</b-list-group-item>
				<b-list-group-item button>I am a button</b-list-group-item>
				<b-list-group-item button>Disabled button</b-list-group-item>
				<b-list-group-item button>This is a button too</b-list-group-item>
			</b-list-group>
		</b-modal>
	</div>
</template>

<script>
import colorPicker from '../helpers/colorPicker'

export default {
	components: {
		colorPicker
	},
	data() {
		return {
			collections: [
				{ root: 'oui', guid: '4sd54fd56s4g', name: 'page', description: 'liste des pages', actions: '' },
				{ root: '', guid: '6s5d4fg56sd4fg', name: 'component', description: 'liste des composants', actions: '' }
			],
			collection: { root: '', guid: '6s5d4fg56sd4fg', name: 'component', description: 'liste des composants', actions: '',
				items:[
					{ id: 'nssfsfsd', require: true, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
					{ id: 'nssfsfsd', require: false, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
					{ id: 'nssfsfsd', require: false, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
					{ id: 'nssfsfsd', require: true, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'object', target: 'kiss:js:vuejs:v2', actions: '' }
				]
			},
			item: { id: 'nssfsfsd', require: true, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
			type_de_vars:[
				{ value: null, text: 'Please select an option' },
				{ value: 'kiss:base_vars:string', text: 'Chaine de characteres' },
				{ value: 'kiss:base_vars:integer', text: 'Valeur entiere' }
			],
		}
	},
	methods: {
		updateItem() {
			this.$bvModal.show('modal-field')
		},
		selectElement() {
			this.$bvModal.show('modal-select-one')
		}
	}
}
</script>

<style scoped>
	.chk{
		padding-left: 10px;
	}
	.element{
		margin-bottom: 20px;
	}
</style>