<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";
import type {ArchiveSchema} from "@/types/output";

const archiveStore = useArchiveStore()
archiveStore.getArchives()

defineProps<{
  archives?: ArchiveSchema[] | null
}>()

</script>

<template>
  <template></template>
  <data-table :value="archives">
    <Column header="Name">
      <template #body="slotProps">
        <RouterLink class="underline" :to="{name: 'search', params: {archiveId: slotProps.data.id}}">
          {{ slotProps.data.name }}
        </RouterLink>

      </template>
    </Column>
    <Column field="createOn" header="Erstellt am"></Column>
    <template #empty="slotProps">
      <div class="p-d-flex p-jc-center">
        Keine Archive vorhanden.
      </div>
    </template>
  </data-table>
</template>

<style scoped>

</style>