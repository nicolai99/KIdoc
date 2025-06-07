<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";

const archiveStore = useArchiveStore();
defineProps({id: Number, type: String, label: String, value: [String, Number], index: Number})
</script>

<template>
  <div v-if="type=='date'">
    <FloatLabel variant="on">
      <DatePicker :value="value">
      </DatePicker>
      <label>{{ label }}</label>
    </FloatLabel>
  </div>
  <div v-else-if="type=='text'">
    <FloatLabel variant="on">
      <InputText v-model="archiveStore.attributeValues[index]"></InputText>
      <label>{{ label }}</label>
    </FloatLabel>
  </div>
  <div v-else-if="type=='number'">
    <FloatLabel variant="on">
      <InputNumber v-model="archiveStore.attributeValues[index]"></InputNumber>
      <label>{{ label }}</label>
    </FloatLabel>
  </div>
</template>

<style scoped>

</style>