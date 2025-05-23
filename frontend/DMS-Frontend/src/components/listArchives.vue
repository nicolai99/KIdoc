<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";

const archiveStore = useArchiveStore()
archiveStore.getArchives()

</script>

<template>
  <data-table :value="archiveStore.archives">
    <Column field="name" header="Name"></Column>
    <Column field="create_on" header="Erstellt am"></Column>
  </data-table>

</template>

<style scoped>

</style>