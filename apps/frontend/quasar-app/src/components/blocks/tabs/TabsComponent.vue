<template>
  <div class="box q-my-lg q-mx-xs">
    <q-card class="my-card" flat bordered>

      <div class="row wrap-md no-wrap-lg items-center title-container">
        <div class="col">
          <q-item>
            <q-item-section avatar>
              <q-avatar icon="newspaper" />
            </q-item-section>

            <q-item-section>
              <q-item-label
                >РИА Новости: Устроивших теракт в «Крокусе» завербовали через
                Telegram-канал ИГ</q-item-label
              >
              <q-item-label caption class="text-red-10">
                Не опубликованные
              </q-item-label>
            </q-item-section>
          </q-item>
        </div>
        <div class="col-auto">
          <q-tabs
            dense
            align="right"
            class="text-black"
            :breakpoint="500"
            no-caps
            content-class="title-tabs"
            inline-label
            narrow-indicator
          >
            <q-route-tab
              :to="{ query: { tab: 'TestPart1' } }"
              exact
              label="Не активные"
            />

            <q-route-tab
              :to="{ query: { tab: 'TestPart2' } }"
              exact
              label="Активные"
            />

            <q-btn-dropdown
              class="title-tabs"
              auto-close
              dense
              no-caps
              stretch
              flat
              label="Ещё"
            >
              <q-list>
                <q-item exact :to="{ query: { tab: 'TestPart1' } }">
                  <q-item-section>Movies</q-item-section>
                </q-item>

                <q-item exact :to="{ query: { tab: 'TestPart4' } }">
                  <q-item-section>Photos</q-item-section>
                </q-item>
              </q-list>
            </q-btn-dropdown>
          </q-tabs>
        </div>
      </div>
      <q-separator />

      <q-card-section class="card-content" horizontal>
        <q-card-section class="col-lg col-sm-12 col-md-8">
          <keep-alive>
            <component :is="part[route.query.tab]"></component>
          </keep-alive>
        </q-card-section>

        <q-separator vertical />

        <q-card-section class="col-lg-3 col-sm-12 col-md-4 col-xl-2 position-relative">
          <q-list class="position-sticky position">
            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="primary" name="local_bar" />
              </q-item-section>

              <q-item-section>
                <q-item-label>Bar XYZ</q-item-label>
                <q-item-label caption>Have a drink.</q-item-label>
              </q-item-section>
            </q-item>

            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="red" name="local_gas_station" />
              </q-item-section>

              <q-item-section>
                <q-item-label>Gas Station</q-item-label>
                <q-item-label caption>Fill your gas tank.</q-item-label>
              </q-item-section>
            </q-item>

            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="amber" name="local_movies" />
              </q-item-section>

              <q-item-section>
                <q-item-label>Cinema XYZ</q-item-label>
                <q-item-label caption>Watch a movie.</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { ref, watch } from "vue";
import TestPart1 from "./TestPart1.vue";
import TestPart2 from "./TestPart2.vue";

const route = useRoute();
const part = { TestPart1, TestPart2 };

watch(
  () => route.query.tab,
  async (newId) => {

  }
);
</script>

<style lang="scss" scoped>
.position-sticky {
  position: sticky;
  top: 5px;
}

@media (max-width: $breakpoint-sm-max) {
  .title-container {
    flex-direction: column;
    padding: 20px 0;
  }
.card-content{
    flex-direction: column-reverse;
  }

}
</style>
