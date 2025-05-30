<script setup lang="ts">

import AppLayout from "@/layouts/AppLayout.vue";
import ListArchives from "@/components/ListArchives.vue";
import {ref} from "vue";
import {useArchiveStore} from "@/stores/archiveStore.ts";

const showNewArchive = ref(false);
const archiveStore = useArchiveStore();
archiveStore.getArchives()
</script>

<template>
  <AppLayout>
    <template #subheader>
      Archive
    </template>
    <template #content>
      <Button @click="showNewArchive=!showNewArchive">Neues Archiv</Button>
      <Dialog v-model:visible="showNewArchive" modal class="w-1/2">
        <template #header>
          <h1 class="text-2xl font-bold">Neues Archiv</h1>
        </template>
        <create-archive
            @afterCreateArchive="showNewArchive=!showNewArchive;archiveStore.getArchives()"></create-archive>

      </Dialog>
      <list-archives :archives="archiveStore.archives"></list-archives>
    </template>

  </AppLayout>
</template>

<style scoped>

</style>