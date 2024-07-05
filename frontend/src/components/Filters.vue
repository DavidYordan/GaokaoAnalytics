<template>
    <v-form>
      <v-text-field
        label="School Name"
        v-model="filters.schoolName"
        @input="updateFilters"
      ></v-text-field>
      <!-- 你可以根据需求添加更多筛选条件 -->
      <v-btn @click="applyFilters">Apply Filters</v-btn>
    </v-form>
  </template>
  
  <script>
  export default {
    name: 'Filters',
    data() {
      return {
        filters: {
          schoolName: ''
        }
      };
    },
    methods: {
      updateFilters() {
        this.$emit('filter-changed', this.filters);
      },
      applyFilters() {
        this.$emit('filter-changed', this.filters);
      }
    }
  };
  </script>
  
  <style scoped>
  .v-form {
    display: flex;
    flex-direction: column;
  }
  
  .v-text-field {
    margin-bottom: 20px;
  }
  
  .v-btn {
    align-self: flex-start;
  }
  </style>
  