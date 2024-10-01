<template>
  <q-layout view="lhh lpr lfr">
    <q-header elevated class="color-bg text-white" height-hint="98">
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
                           v-if="authStore.user"
                            color="primary"
                            round
                            outline
                            dense
                            flat
                            square
                            fab-mini
                            icon="note_add"
                            class="q-mr-xs"
                          >
                            <q-menu>
                              <q-list dense style="min-width: 100px">
                                <q-item
                                  clickable
                                  @click="newsStore.open_add_news = true"
                                  v-close-popup
                                >
                                  <q-item-section>Новость</q-item-section>
                                </q-item>
                                <q-item clickable v-close-popup>
                                  <q-item-section>Категорию к новости</q-item-section>
                                </q-item>
                                <q-separator />
                                <q-item clickable to="/desk/realEstate/links/add-new-ads-home">
                                  <q-item-section>Объявление</q-item-section>
                                </q-item>
                                <q-separator />
                                <q-item clickable v-close-popup>
                                  <q-item-section>Админка</q-item-section>
                                </q-item>
                              </q-list>
                            </q-menu>
                          </q-btn>
                          <q-btn
                            v-if="!authStore.user"
                            color="primary"
                            outline
                            dense
                            flat
                            square
                            fab-mini
                            icon="login"
                          >
                            <q-menu>
                              <div class="row no-wrap q-pa-lg">
                                <div class="column">
                                  <div class="text-h6 q-mb-md">Авторизация</div>
                                  <q-btn
                                    color="primary"
                                    label="Вход"
                                    push
                                    square
                                    icon="login"
                                    to="/login"
                                    size="sm"
                                    class="q-ma-xs q-px-xs"
                                    v-close-popup
                                  />
                                  <q-btn
                                    color="primary"
                                    label="Регистрация"
                                    push
                                    outline
                                    square
                                    to="/registration"
                                    size="sm"
                                    icon="person_add"
                                    class="q-ma-xs q-px-xs shadow-0"
                                    v-close-popup
                                  />
                                </div>

                                <q-separator vertical inset class="q-mx-lg" />

                                <div class="column justify-center items-center">
                                  <q-avatar
                                    size="72px"
                                    color="primary"
                                    text-color="white"
                                    icon="admin_panel_settings"
                                  />
                                </div>
                              </div>
                            </q-menu>
                          </q-btn>
                          <q-btn
                            v-if="authStore.user"
                            color="primary"
                            outline
                            dense
                            flat
                            square
                            fab-mini
                            icon="account_circle"
                          >
                            <q-menu>
                              <div class="row no-wrap q-pa-md">
                                <div class="column">
                                  <div class="text-h6 q-mb-md">Аккаунт</div>
                                  <q-btn
                                    color="primary"
                                    label="Профиль"
                                    outline
                                    push
                                    size="sm"
                                    class="q-mt-sm"
                                    v-close-popup
                                  />
                                  <q-btn
                                    color="primary"
                                    outline
                                    label="Кабинет"
                                    push
                                    size="sm"
                                    class="q-mt-sm"
                                    v-close-popup
                                  />
                                </div>

                                <q-separator vertical inset class="q-mx-lg" />

                                <div class="column items-center">
                                  <q-avatar size="72px" color="secondary" icon="person">
                                  </q-avatar>

                                  <div class="text-subtitle1 q-mt-md q-mb-xs">
                                    {{ authStore.user.username }}
                                  </div>

                                  <q-btn
                                    color="primary"
                                    label="Выход"
                                    push
                                    to="/logout"
                                    size="sm"
                                    v-close-popup
                                  />
                                </div>
                              </div>
                            </q-menu>
                          </q-btn>
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
      <promo-header />
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
import { useAuthStore } from "src/stores/all";
import { ref, onMounted  } from "vue";
import MainMenu from "components/navigation/MainMenu.vue";
import SubMenu from "components/navigation/SubMenu.vue";
import PartLeft from "components/parts/PartLeft.vue";
import PromoHeader from "components/blocks/promo/PromoHeader.vue";

const leftDrawerOpen = ref(false);
const rightDrawerOpen = ref(false);

const authStore = useAuthStore();

// Проверяем, авторизован ли пользователь
onMounted(async () => {
  if (!authStore.user) {
    await authStore.getAuthUser(); // Получаем текущего пользователя, если он не загружен
  }
});

const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value;
};

const toggleRightDrawer = () => {
  rightDrawerOpen.value = !rightDrawerOpen.value;
};
</script>
<style></style>
