<template>
  <q-layout view="lhh lpr lfr">
    <q-header elevated class="bg-secondary text-white" height-hint="98">
      <q-toolbar>
        <q-btn
          dense
          flat
          round
          icon="menu"
          color="primary"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          <main-menu />
        </q-toolbar-title>

        <q-btn
          dense
          flat
          round
          icon="menu"
          color="primary"
          @click="toggleRightDrawer"
        />
      </q-toolbar>
      <sub-menu />
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>
      <PartLeft />
    </q-drawer>

    <q-drawer v-model="rightDrawerOpen" side="right" overlay bordered>
      <!-- drawer content -->
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          <div>Title</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref } from "vue";
import MainMenu from "components/navigation/MainMenu.vue";
import SubMenu from "components/navigation/SubMenu.vue";
import PartLeft from "components/parts/PartLeft.vue";

const leftDrawerOpen = ref(false);
const rightDrawerOpen = ref(false);

const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value;
};

const toggleRightDrawer = () => {
  rightDrawerOpen.value = !rightDrawerOpen.value;
};
</script>
<style></style>
