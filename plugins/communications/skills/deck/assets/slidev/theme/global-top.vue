<script setup>
import { computed } from 'vue'
const cfg = $slidev.configs
const layout = computed(() => $slidev.nav.currentLayout)
const isTitle = computed(() => layout.value === 'op-title')
const isSection = computed(() => layout.value === 'op-section')
</script>

<template>
  <div class="op-chrome" :class="[cfg.audience, { 'on-dark': isSection }]">
    <div class="op-header">{{ cfg.header }}</div>
    <div class="op-footer">{{ cfg.footer }}</div>
    <div v-if="!isTitle" class="op-page">{{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}</div>
  </div>
</template>
