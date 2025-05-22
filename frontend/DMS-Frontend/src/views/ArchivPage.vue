<script setup lang="ts">

import AppLayout from "@/layouts/AppLayout.vue";
import ListArchives from "@/components/listArchives.vue";
</script>

<template>
  <AppLayout>
    <template #subheader>
      Archive
    </template>
    <template #content>
      <list-archives></list-archives>
    </template>
    
  </AppLayout>
</template>

<style scoped>

</style>