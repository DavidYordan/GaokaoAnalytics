<template>
    <div id="app">
      <v-app>
        <v-app-bar app color="primary" dark>
          <v-toolbar-title>Gaokao Analytics</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn text to="/">Home</v-btn>
          <v-btn text to="/special-score">Special Scores</v-btn>
          <v-btn text to="/special-plan">Special Plans</v-btn>
        </v-app-bar>
        <v-main>
          <v-container fluid>
            <router-view></router-view>
          </v-container>
        </v-main>
        <v-footer app color="primary" dark>
          <span class="white--text">&copy; 2024 Gaokao Analytics</span>
        </v-footer>
      </v-app>
    </div>
  </template>
  
  <script>
  export default {
    name: 'App',
  };
  </script>
  
  <style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  