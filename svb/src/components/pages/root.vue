<template>
  <div>
<<<<<<< HEAD
    <div class="root_message">message</div>
    <b-row>
      <b-col>col</b-col>
      <b-col>col</b-col>
      <b-col>col</b-col>
      <b-col>col</b-col>
=======
    <b-row>
      <b-col>
        <div class="message">
          Aucun projet n'a été detecté dans le repertoire <span class="path">/qdsq/qsdqsd/qsdqsd</span><br/>
          Assurez vous d'avoir bien réalisé un lien vers un fichier KissTomato depuis l'extérieur du container.<br/>
          <div class="code">
            CODE ICI mapping volume
          </div>
          Ou, utilisez l'assitant pour créer un nouveau projet.
        </div>
      </b-col>
    </b-row>
    <b-row>
      <b-col><b-button variant="primary"><b-icon icon="plus-circle"></b-icon> Creer un nouveau projet</b-button></b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-table striped hover :items="items" caption-top>
          <template #table-caption>Liste des projets</template>
          <template #cell(actions)="data">
            <b-button variant="success" title="Selectionner le projet"><b-icon icon="wallet"></b-icon>{{ data.item.id }}</b-button>
            <b-button variant="warning" title="Exporter le projet"><b-icon icon="box-arrow-up"></b-icon></b-button>
            <b-button variant="danger" title="Supprimer le projet"><b-icon icon="trash2"></b-icon></b-button>
          </template>
        </b-table>
      </b-col>
>>>>>>> ffb9697e69e3fe2d16935fc8a8535647447fb395
    </b-row>
  </div>
</template>

<script>
<<<<<<< HEAD
export default {}
</script>

<style scoped>
  .root_message{
    border: 1px solid red;
    border-radius: 20px;
=======
export default {
  data() {
    return {
      items: [
        { id: 40, nom: 'Dickerson', description: 'Macdonald dfg  sdfg sdf sd fgsd fsdf  dsfgs dfg dsf gd fsd sd fgds fgsd fgdsf gd fdsf gs fgsd fges r gs drs gdrs vdsr vsr vsdr vsdrv rdvdrv dsr vr drsv sd vsdrvsdvsdacdonald dfg  sdfg sdf sd fgsd', Actions: '' },
        { id: 21, nom: 'Larsen', description: 'Shaw dfg  sdfg sdf sd fgsd fsdf  dsfgs dfg dsf gd fsd sd fgds fgsd fgdsf gd fdsf gs fgsd fges r gs drs gdrs vdsr vsr vsdr vsdrv rdvdrv dsr vr drsv sd vsdrvsdvsd', Actions: '' },
        { id: 89, nom: 'Geneva', description: 'Wilson dfg  sdfg sdf sd fgsd fsdf  dsfgs dfg dsf gd fsd sd fgds fgsd fgdsf gd fdsf gs fgsd fges r gs drs gdrs vdsr vsr vsdr vsdrv rdvdrv dsr vr drsv sd vsdrvsdvsd', Actions: '' },
        { id: 38, nom: 'Jami', description: 'Carney dfg  sdfg sdf sd fgsd fsdf  dsfgs dfg dsf gd fsd sd fgds fgsd fgdsf gd fdsf gs fgsd fges r gs drs gdrs vdsr vsr vsdr vsdrv rdvdrv dsr vr drsv sd vsdrvsdvsd', Actions: '' }
      ]
    }
  }
}
</script>

<style scoped>
  .message{
    border: 1px solid #f7786f;
    background-color: #edccca;
    border-radius: 5px;
    padding: 5px;
    margin-bottom: 20px;
  }
  .path{
    border: 1px solid #68e330;
    background-color: #d1ebc5;
    border-radius: 3px;
    width: fit-content;
    padding: 0 5px;
  }
  .code{
    border: 1px solid #979c92;
    background-color: #dfe0de;
    border-radius: 3px;
    width: fit-content;
    padding: 5px;
    margin: 20px 0;
>>>>>>> ffb9697e69e3fe2d16935fc8a8535647447fb395
  }
</style>
