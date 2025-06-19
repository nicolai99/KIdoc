<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";

const archiveStore = useArchiveStore();
defineProps({id: Number, type: String, label: String, index: Number})
</script>

<template>
  <div v-if="type=='date'">
    <FloatLabel variant="on">
      <DatePicker v-model="archiveStore.attributeValues[index]" dateFormat="dd.mm.yy">
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
      <InputNumber v-model="archiveStore.attributeValues[index]" :use-grouping="false"
                   :min-fraction-digits=2></InputNumber>
      <label>{{ label }}</label>
    </FloatLabel>
  </div>
</template>

<style scoped>

</style>