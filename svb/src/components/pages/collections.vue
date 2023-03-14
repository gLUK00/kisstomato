<template>
<<<<<<< HEAD
  <div>
    <h1>Collections</h1>
  </div>
</template>

<script>
export default { }
</script>
=======
	<div>
		<h1>Collections du projet</h1>
		<div style="border:1px solid red;">
			<b-button variant="secondary" title="Supprimer le projet"><b-icon icon="arrow-left"></b-icon> Annuler</b-button>
			<b-button variant="success" title="Supprimer le projet"><b-icon icon="arrow-counterclockwise"></b-icon> Valider</b-button>
		</div>
		<div style="border:1px solid red;">
			<b-table striped hover :items="collections" caption-top :fields="show_fields">
				<template #cell(guid)="data">
					<span class="tagColor" :style="'background-color:#' + data.item.color">{{ data.item.guid }}</span>
				</template>
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
			<colorPicker :color="collection.color" @update-color="setColor"/>
			<!-- mise en place des limites -->
			<b-table striped hover :items="collection.items" :fields="['guid','require','name','description','type','actions']" caption-top>
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
				<template #cell(name)="data">
					<span v-if="data.item.nodename" class="tagColor" style="border:1px solid #ccc">{{ data.item.name }}</span>
					<span v-else>{{ data.item.name }}</span>
				</template>
			</b-table>
			<b-button variant="success" title="Ajouter un élément"><b-icon icon="plus-circle"></b-icon> Ajouter un élément</b-button>
		</div>
		<b-modal id="modal-field" size="xl" :title="'guid : ' + item.guid" no-close-on-backdrop="true" hide-header-close="true">
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
					<label><input type="radio" v-model="item.type" value="list"/> Liste</label>
					<label><input type="radio" v-model="item.type" value="object"/> Objet</label>
					<label><input type="radio" v-model="item.type" value="objects"/> Collection d'objets</label>
				</div>
				<b-form-group v-if="item.type == 'variable'" class="element" label="Type de variable :">
					<b-form-select v-model="item.target" :options="type_de_vars"></b-form-select>
				</b-form-group>
				<div v-if="item.type != 'variable'">
					<span>Objet séléctionné :</span>
					<div>
						<listSelector :items="collections" :target="item.target" title="Liste des objets" keyId="id" keyName="name" keyColor="color" @select-item="setTarget"/>
					</div>
				</div>
			</b-form>
		</b-modal>
	</div>
</template>

<script>
import colorPicker from '../helpers/colorPicker'
import listSelector from '../helpers/listSelector'

export default {
	components: {
		colorPicker, listSelector
	},
	data() {
		return {
			show_fields: ['racine', 'guid', 'name', 'description', 'actions'],
			collections: [
				{ color: '3ff2e9', racine: '(root)', guid: '4sd54fd56s4g', name: 'page', description: 'liste des pages', actions: '' },
				{ color: 'e3e635', racine: 'page', guid: '6s5d4fg56sd4fg', name: 'component', description: 'liste des composants', actions: '' }
			],
			collection: { racine: '', guid: '6s5d4fg56sd4fg', name: 'component', description: 'liste des composants', actions: '', color: '3ff2e9',
				items:[
					{ guid: 'nssfsfsd', nodename: true, require: true, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
					{ guid: 'nssfsfsd', require: false, name: 'component aa', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
					{ guid: 'nssfsfsd', require: false, name: 'component bb', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
					{ guid: 'nssfsfsd', require: true, name: 'component cc', description: 'dsf qsdfqs fsqdfqsd', type: 'object', target: 'kiss:js:vuejs:v2', actions: '' }
				]
			},
			item: { guid: 'nssfsfsd', require: true, name: 'sdfsdfsdf', description: 'dsf qsdfqs fsqdfqsd', type: 'variable', target: 'kiss:base_vars:integer', actions: '' },
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
		setColor( itemColor ) {
			this.collection.color = itemColor
		},
		setTarget( selectItem ){
			this.item.target = selectItem
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
	.tagColor{
		padding: 3px 5px;
		border-radius: 7px;
	}
</style>
>>>>>>> ffb9697e69e3fe2d16935fc8a8535647447fb395
