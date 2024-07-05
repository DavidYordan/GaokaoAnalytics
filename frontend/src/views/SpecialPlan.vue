<template>
    <v-container>
      <v-row>
        <v-col>
          <Filters @filter-changed="handleFilterChange" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <DataTable :filters="filters" apiEndpoint="special-plan" />
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import Filters from '@/components/Filters.vue';
  import DataTable from '@/components/DataTable.vue';
  
  export default {
    name: 'SpecialPlan',
    components: {
      Filters,
      DataTable
    },
    data() {
      return {
        filters: {}
      };
    },
    methods: {
      handleFilterChange(newFilters) {
        this.filters = newFilters;
      }
    }
  };
  </script>
  
  <style scoped>
  .v-container {
    padding-top: 20px;
  }
  
  .v-row {
    margin-bottom: 20px;
  }
  
  .v-col {
    padding: 0 10px;
  }
  
  .v-btn {
    margin-top: 10px;
  }
  </style>
  