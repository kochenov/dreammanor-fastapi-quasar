<template>
  <q-tabs
    align="left"
    id="topmenu"
    dense
    inline-label
    indicator-color="primary"
    class="primary text-primary"
    narrow-indicator
    shrink
    outside-arrows
    mobile-arrows
  >
    <q-route-tab
      v-for="item in topmenu"
      :to="item.name == 'home' ? '/' : { query: { submenu: item.name } }"
      :key="item.id"
      exact
      :icon="item.icon"
      :label="item.label"
    />
  </q-tabs>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { LocalStorage } from "quasar";

const topmenu = ref("");

onMounted(() => {
  let top_menu = LocalStorage.getItem("topmenu");
  if (!top_menu) {
    axios
      .get("/data/main-nav.json")
      .then((response) => {
        topmenu.value = response.data;
        LocalStorage.set("topmenu", topmenu.value);
      })
      .catch((error) => {
        console.error("Ошибка при получении данных", error);
      });
  } else {
    topmenu.value = top_menu;
  }
});
</script>

<style lang="scss">
#topmenu {
  .q-tab {
    min-height: 48px !important;
  }
  .q-tab__indicator {
    height: 8px;
  }
  .q-tab:hover {
    .q-tab__indicator {
      opacity: 1 !important;
    }
  }
  .q-hoverable:hover > .q-focus-helper {
    background: currentColor;
    opacity: 0 !important;
  }

  .q-tab__label,
  .q-tab__icon {
    font-weight: 600;
  }
  .q-tab__label {
    font-size: 12px;
  }

  .q-tab__icon {
    font-size: 14px;
  }
}
</style>
