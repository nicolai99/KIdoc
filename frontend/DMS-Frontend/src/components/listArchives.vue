<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";

const archiveStore = useArchiveStore()
archiveStore.getArchives()

</script>

<template>
  <p v-for="archive in archiveStore.archives">
    {{ archive.name }}
  </p>
</template>

<style scoped>

</style>