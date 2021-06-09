<template>
  <div id="app">
    <b-navbar type="dark" variant="success">
      <b-navbar-nav>
        <b-nav-item tag="h1" href="#/"><b-icon icon="house"></b-icon> KissTomato</b-nav-item>
        <b-nav-item href="#/project"><b-icon icon="box-seam"></b-icon> Project XXXXX</b-nav-item>
        <b-nav-item href="#/collections"><b-icon icon="list-stars"></b-icon> Collections</b-nav-item>
        <b-nav-item href="#/data"><b-icon icon="bar-chart-steps"></b-icon> Data</b-nav-item>
        <b-nav-item href="#/templates"> <b-icon icon="layout-text-window-reverse"></b-icon>Templates</b-nav-item>
        <b-nav-item disabled href="#/merges"><b-icon icon="front"></b-icon> Merges</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <b-container class="pos_container">
      <router-view/>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;*/
}
.pos_container{
  margin-left: 5px;
  margin-right: 5px;
  margin-top: 5px;
  max-width: initial;
}
</style>
