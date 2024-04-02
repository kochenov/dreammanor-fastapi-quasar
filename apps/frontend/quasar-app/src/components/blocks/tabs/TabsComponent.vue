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
                >Объявления для парсинга
                <q-badge outline v-if="parserStore.parser_links" align="middle" color="primary">
                  {{ parserStore.parser_links.total || '0'}}
                </q-badge>
              </q-item-label>
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
              class="title-tabs q-mr-lg"
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

        <q-card-section
          class="col-lg-3 col-sm-12 col-md-4 col-xl-2 position-relative"
        >
          <q-list class="position-sticky position">
            <!-- -->

            <!-- -->
            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-icon color="primary" name="smart_display" />
              </q-item-section>

              <q-item-section>
                <q-item-label>Видео</q-item-label>
              </q-item-section>
              <q-item-section side>
                <q-toggle
                  color="blue"
                  @click="getListAsd()"
                  v-model="parserStore.filters.is_video"
                  val="battery"
                />
              </q-item-section>
            </q-item>

            <q-expansion-item
              expand-separator
              icon="payments"
              label="Диапазон цен"
            >
              <q-card>
                <q-card-section>
                  Цена от {{ price.min }} до {{ price.max }} руб
                  <q-range
                    @change="updatePriceFilter()"
                    v-model="price"
                    :min="0"
                    :max="3000000"
                    :step="50000"
                  />
                </q-card-section>
              </q-card>
            </q-expansion-item>
            <q-expansion-item
              expand-separator
              icon="new_releases"
              label="Статус объявлений"
            >
              <q-select
                v-model="parserStore.filters.status_id"
                @update:model-value="getListAsd()"
                emit-value
                map-options
                :options="status_options"
                label="Выбери статус"
            /></q-expansion-item>
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
import { useRealEstateParserStore } from "src/modules/real_estate";

const route = useRoute();
const part = { TestPart1, TestPart2 };
const price = ref({
  min: 100000,
  max: 650000,
});
const status_options = ref([
  {
    label: "Не опубликован",
    value: 0,
  },
  {
    label: "Не подходит",
    value: 2,
  },
  {
    label: "Вертикальное видео",
    value: 3,
  },
  {
    label: "Чёрный список",
    value: 4,
  },
]);

const parserStore = useRealEstateParserStore();

const getListAsd = async () => {
  await parserStore.getLinks();
  //items.value = parserStore.parser_links.items;
};

const updatePriceFilter = async () => {
  parserStore.filters.max_price = price.value.max;
  parserStore.filters.min_price = price.value.min;
  await getListAsd();
};
watch(
  () => route.query.tab,
  async (newId) => {}
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
  .card-content {
    flex-direction: column-reverse;
  }
}
</style>
