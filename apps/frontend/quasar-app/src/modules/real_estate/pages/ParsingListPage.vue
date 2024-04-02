<template>
  <q-page class="">
    <page-card
      page_title="Объявления для парсинга"
      :page_subtitle="
        status_options.find(
          (option) => option.value === parser.filters.status_id
        )?.label || 'Не активные'
      "
      icon_title="newspaper"
      :total="parser.parser_links ? parser.parser_links.total : 0"
    >
      <!-- -->
      <template v-slot:side_right>
        <q-list class="position-sticky position">
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
                @click="getLinks()"
                v-model="parser.filters.is_video"
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
                  :max="1500000"
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
              v-model="parser.filters.status_id"
              @update:model-value="getLinks()"
              emit-value
              map-options
              :options="status_options"
              label="Выбери статус"
          /></q-expansion-item>
        </q-list>
      </template>
      <!-- -->
      <template v-slot:main_content>
        <div v-if="parser.error.length > 0">
          <q-banner
            v-for="i in parser.error"
            :key="i"
            inline-actions
            class="text-white bg-red"
          >
            {{ i }}
            <template v-slot:action>
              <q-btn
                flat
                color="white"
                @click="clearFilters()"
                label="Сбросить фильтр"
              />
            </template>
          </q-banner>
        </div>
        <!-- -->

        <div v-if="!parser.loading" class="row-grid">
          <ItemCard
            @edit-item="updateItem"
            @add-comment="addComment"
            v-for="item in parser.parser_links ? parser.parser_links.items : []"
            :item="item"
            :key="`${item.link}`"
          />
        </div>
        <div v-else class="row-grid">
          <q-card v-for="n in 6" :key="n">
            <q-skeleton height="200px" square />
            <q-item>
              <q-item-section>
                <q-item-label>
                  <q-skeleton type="text" />
                </q-item-label>
                <q-item-label caption>
                  <q-skeleton type="text" />
                </q-item-label>
                <q-item-label caption align="right">
                  <q-skeleton
                    type="text"
                    width="20%"
                    class="text-subtitle1 text-right"
                  />
                </q-item-label>
              </q-item-section>
            </q-item>

            <q-card-actions align="right" class="q-gutter-md">
              <q-skeleton type="QBtn" />
              <q-skeleton type="QBtn" />
            </q-card-actions>
          </q-card>
        </div>
      </template>
    </page-card>
    <q-dialog v-model="edit_form_comment_flag" persistent>
      <q-card style="min-width: 300px">
        <q-card-section>
          <div class="text-h6">Your address</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-select
            v-model="edit_form_comment.status_id"
            emit-value
            map-options
            :options="status_options"
            label="Изменить статус"
          />
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="edit_form_comment.comment" autofocus />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Отмена" v-close-popup />
          <q-btn
            flat
            label="Изменить"
            @click="updateItem(edit_form_comment)"
            v-close-popup
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import PageCard from "components/main/page/PageCard.vue";
import ItemCard from "../components/ItemCard.vue";
import { useRealEstateParserStore as parserStore } from "../index";
import { onMounted, ref } from "vue";

// Pinia
const parser = parserStore();
// Flags
const edit_form_comment_flag = ref(false);
// edit form
const edit_form_comment = ref({
  status_id: null,
  comment: null,
  id: null,
});
// Фильтры
const price = ref({
  min: 100000,
  max: 650000,
});
const status_options = ref([
  {
    label: "Не активные",
    value: 0,
  },
  {
    label: "Активные",
    value: 1,
  },
  {
    label: "Уточняю информацию",
    value: 2,
  },
  {
    label: "Вертикальное видео",
    value: 3,
  },
  {
    label: "Не подходит",
    value: 4,
  },
]);

onMounted(async () => {
  await getLinks();
});

const getLinks = async () => {
  await parser.getLinks();
};

const updatePriceFilter = async () => {
  parser.filters.max_price = price.value.max;
  parser.filters.min_price = price.value.min;
  await getLinks();
};

const clearFilters = async () => {
  parser.cleanFilters();
  await getLinks();
};

const updateItem = async (data) => {
  await parser.updateLink(data);
};
const addComment = async (item) => {
  edit_form_comment_flag.value = true;
  edit_form_comment.value.comment = item.comment;
  edit_form_comment.value.status_id = item.status_id;
  edit_form_comment.value.id = item.id;
};
</script>
<style lang="scss" scoped>
.row-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
  justify-content: center;
}

.position-sticky {
  position: sticky;
  top: 5px;
}
</style>
