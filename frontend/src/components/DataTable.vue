<template>
    <v-data-table
      :headers="headers"
      :items="items"
      :items-per-page="100"
      class="elevation-1"
    ></v-data-table>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'DataTable',
    props: {
      filters: {
        type: Object,
        default: () => ({})
      },
      apiEndpoint: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        headers: [],
        items: []
      };
    },
    watch: {
      filters: {
        handler: 'fetchData',
        deep: true
      }
    },
    created() {
      this.setHeaders();
      this.fetchData();
    },
    methods: {
      setHeaders() {
        if (this.apiEndpoint === 'special-score') {
          this.headers = [
            { text: 'School', value: 'school' },
            { text: 'Score', value: 'score' }
            // 根据实际情况添加更多列
          ];
        } else if (this.apiEndpoint === 'special-plan') {
          this.headers = [
            { text: 'School', value: 'school' },
            { text: 'Plan', value: 'plan' }
            // 根据实际情况添加更多列
          ];
        }
      },
      fetchData() {
        axios.get(`http://localhost:5000/api/${this.apiEndpoint}`, { params: this.filters })
          .then(response => {
            this.items = response.data;
          })
          .catch(error => {
            console.error("There was an error!", error);
          });
      }
    }
  };
  </script>
  
  <style scoped>
  .v-data-table {
    margin-top: 20px;
  }
  </style>
  