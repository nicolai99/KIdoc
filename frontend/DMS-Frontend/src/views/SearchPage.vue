<script setup lang="ts">

import AppLayout from "@/layouts/AppLayout.vue";
import {useArchiveStore} from "@/stores/archiveStore.ts";
import SearchDocs from "@/components/SearchDocs.vue";
import {useRoute} from "vue-router";


const archiveStore = useArchiveStore();
const route = useRoute();
const archiveId = Number(route.params.archiveId);
archiveStore.getArchiveById(archiveId)
</script>

<template>
  <AppLayout>
    <template #subheader>
      <h1>Suche</h1>
    </template>
    <template #content>
      <searchDocs :archive="archiveStore.archive"
                  :lengthAttributes="archiveStore.archive.attributes.length!"></searchDocs>
    </template>
  </AppLayout>
</template>

<style scoped>

</style>