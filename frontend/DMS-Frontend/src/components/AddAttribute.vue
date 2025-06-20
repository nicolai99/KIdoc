<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";
import type {AttributesSchema} from "@/types/output";
import {ref} from "vue";

const archivStore = useArchiveStore();
archivStore.getTypes();
const attribute = ref<AttributesSchema>({
  label: '',
  name: '',
  type: {
    id: 0,
  }
});
const emit = defineEmits(['afterAddAttribute'])
const addAttribute = () => {
  emit('afterAddAttribute', attribute.value);
}

</script>

<template>
  <div class="grid grid-cols-1 gap-y-2 p-2">
    <FloatLabel variant="on">
      <InputText id="label" v-model="attribute.label"
                 @keyup="attribute.name=attribute.label.toLowerCase()"/>
      <label for="label">Label</label>
    </FloatLabel>
    <FloatLabel variant="on">
      <InputText id="name" v-model="attribute.name"/>
      <label for="name">Name</label>
    </FloatLabel>
    <FloatLabel variant="on">
      <Select v-model="attribute.type.id" inputId="over_label" :options="archivStore.types"
              optionLabel="name"
              optionValue="id"
              class="w-full"/>
      <label for="name">Feldart</label>
    </FloatLabel>
    <Button @click="addAttribute">Attribut hinzufügen</Button>
  </div>
</template>

<style scoped>

</style>