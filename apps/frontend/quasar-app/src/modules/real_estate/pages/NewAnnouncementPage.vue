<template>
  <page-card
    page_title="Добавить новое объявление"
    page_subtitle="Черновик"
    icon_title="newspaper"
    :side_right="false"
  >
    <template v-slot:head_nav_right>
      <q-btn
        class="q-mr-md"
        outline
        color="secondary"
        label="Загрузить данные"
      />
    </template>
    <template v-slot:main_content>
      <q-form>
        <q-stepper v-model="step" vertical color="primary" animated>
          <q-step
            :name="1"
            title="Место расположения дома"
            icon="settings"
            caption="Указать регион, район и название поселения, улицу и дом"
            :done="step > 1"
          >
            <!--Карточка в списке-->

            <add-location />

            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.full_adress &&
                  form_data.region &&
                  form_data.district &&
                  form_data.settlement_type &&
                  form_data.settlement
                    ? (step = 2)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step
            :name="2"
            title="Основные характеристики дома"
            caption="Ввести площадь дома, площадь участка, цену на дом, наличие комуникаций"
            icon="create_new_folder"
            :done="step > 2"
          >
            <div class="row q-mt-sm wrap q-col-gutter-md">
              <!-- Цена дома -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.price"
                label="Цена дома"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Площадь дома -->
              <q-input
                class="col-12 col-sm"
                filled
                type="number"
                v-model="form_data.area_of_house"
                label="Площадь дома"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Площадь участка  -->
              <q-input
                class="col-12 col-sm"
                filled
                type="number"
                v-model="form_data.plot_area"
                label="Площадь участок"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
            </div>
            <!-- Характеристики дополнительные -->
            <q-toggle
              v-model="form_data.bathroom_in_house"
              label="Туалет дома"
              color="green"
              checked-icon="check"
              unchecked-icon="clear"
            />
            <!-- Газ -->
            <q-toggle
              v-model="form_data.gaz"
              label="Газ"
              color="green"
              checked-icon="check"
              unchecked-icon="clear"
            />

            <q-separator color="orange q-mt-lg" inset />

            <h6>Количество комнат</h6>
            <!-- количество комнат -->
            <div class="q-gutter-sm">
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="1"
                label="1 комната"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="2"
                label="2 комнаты"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="3"
                label="3 комнаты"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="4"
                label="4 комнаты"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="5"
                label="5 комнат"
              />
            </div>

            <h6>Количество этажей</h6>
            <!-- количество этажей -->
            <div class="q-gutter-sm">
              <q-radio
                v-model="form_data.number_of_floors"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="1"
                label="1 этаж"
              />
              <q-radio
                v-model="form_data.number_of_floors"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="2"
                label="2 этажа"
              />
              <q-radio
                v-model="form_data.number_of_floors"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="3"
                label="3 этажа"
              />
            </div>

            <h6>Дополнительные параметры объявления</h6>
            <!-- количество этажей -->
            <div class="column q-gutter-sm q-mb-md">
              <!-- Пластиковые окна -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.plastic_windows"
                label="Пластиковые окна"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Характеристики основные  -->
              <!-- Наличие бани -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.sauna"
                label="Баня"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- автобусная остановка -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.bus_stop"
                label="Наличие автобусной остановки"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие ж/д станции -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.rail_station"
                label="Наличие ж/д остановки"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие рядом леса -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.there_is_a_forest_nearby"
                label="Наличие рядом леса"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие газового отопления -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.gas_heating"
                label="Наличие газового отопления"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие печного отопления -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.furnace_heating"
                label="Наличие печного отопления"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие канализации -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.sewerage"
                label="Наличие канализации"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Аварийный дом -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.alarm_status"
                label="Аварийное состояние дома"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />
            </div>
            <div class="row q-mt-sm wrap q-col-gutter-md">
              <!-- Расстояние до реки -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.distance_to_the_river"
                label="Расстояние до реки"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Расстояние до озера -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.distance_to_the_lake"
                label="Расстояние до озера"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Расстояние до города -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.distance_to_the_city"
                label="Расстояние до города"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- год постройки -->
              <q-input
                class="col-12 col-sm"
                filled
                hint="Год: XXXX"
                v-model="form_data.year_of_construction"
                label="Год постройки"
                type="number"
                :min="1901"
                :max="curr_yaer"
                lazy-rules
                :rules="[
                  (val) =>
                    (val > 1900 && val <= curr_yaer) ||
                    'Число должно быть больше 1900 и не больше ' + curr_yaer,
                ]"
              />

              <!-- Материал стен -->
              <q-input
                class="col-12 col-sm"
                fille
                v-model="form_data.wall_material_id"
                label="Материал стен"
                type="number"
              />
            </div>
            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.plot_area &&
                  form_data.price &&
                  form_data.area_of_house
                    ? (step = 3)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
              <q-btn
                flat
                @click="step = 1"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step
            :name="3"
            title="Видео обзоры"
            caption="Ссылки на объявление и видео ролик "
            icon="create_new_folder"
            :done="step > 3"
          >
            <!-- Ссылка на объявление -->
            <q-input
              class="q-my-md"
              type="url"
              aria-required
              filled
              v-model="form_data.link_to_ads"
              label="Ссылка на объявление"
              hint="Ссылка на объявление для автоматической переадресации"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Заполнять обязательно',
              ]"
            />
            <!-- Видео Дзен -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.video_zen"
              label="Видео рилик из Dzen"
              hint="Ввести код"
              lazy-rules
            />
            <!-- Видео Рутуб -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.video_rutube"
              label="Видео рилик из Рутуб"
              hint="Ввести код"
              lazy-rules
            />

            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.full_adress &&
                  form_data.link_to_ads &&
                  (form_data.video_zen || form_data.video_rutube)
                    ? (step = 4)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
              <q-btn
                flat
                @click="step = 2"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step
            :name="4"
            title="Название и описание"
            caption="Написать описание к объявлению и видео обзору"
            icon="create_new_folder"
            :done="step > 4"
          >
            <!-- Заголовок -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.title"
              label="Заголовок объявления *"
              hint="Для привлечения внимания"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length < 200) ||
                  'Заголовок обязателен для заполнения',
              ]"
            />
            <!-- Мета Заголовок -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.meta_title"
              label="Заголовок Meta-Title *"
              hint="Для SEO"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length < 200) ||
                  'Заголовок обязателен для заполнения',
              ]"
            />
            <!-- Описание -->
            <q-editor
              v-model="form_data.description"
              @blur="textClean()"
              paragraph-tag="p"
              :toolbar="[['bold', 'italic']]"
              min-height="5rem"
            />
            <!--  <q-input
              class="q-my-md"
              filled
              v-model="form_data.description"
              type="textarea"
              label="Описание к объявлению *"
              hint="Показывается на странице объявления"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Заполнять обязательно',
              ]"
            /> -->
            <!-- Описание -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.meta_description"
              type="textarea"
              label="Мета Описание *"
              hint="SEO"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length < 500) ||
                  'Заголовок обязателен для заполнения',
              ]"
            />

            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.title && form_data.description
                    ? (step = 5)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
              <q-btn
                flat
                @click="step = 3"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step :name="5" title="Публикация материала" icon="add_comment">
            <!---->
            <q-uploader
              @added="initImage"
              :auto-upload="false"
              :multiple="false"
              accept=".jpg, .jpeg, .png"
              hide-upload-btn
              label="Картинка карточки"
            />
            <!--UID-->
            <div class="row">
              <q-input
                class="q-my-md col-md-3 col-sm-12"
                filled
                v-model="form_data.uid"
                type="number"
                label="Уникальный код *"
                hint="Код по которому можно найти объявление"
                lazy-rules
                :rules="[
                  (val) =>
                    (val && val.length > 0) || 'Обязателен для заполнения',
                ]"
              />
            </div>

            <!-- Вкл черновик -->
            <q-toggle
              v-model="form_data.status"
              label="Опубликовать объявление"
              color="green"
              checked-icon="check"
              unchecked-icon="clear"
            />
            <q-stepper-navigation>
              <q-btn color="primary" @click="onSubmit" label="Публиковать" />
              <q-btn
                flat
                @click="step = 4"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>
        </q-stepper>
      </q-form>
    </template>
  </page-card>
</template>

<script setup>
import PageCard from "src/components/main/page/PageCard.vue";
import AddLocation from "../components/form/create/AddLocation.vue"
import { ref, watch, onMounted, computed } from "vue";

const step = ref(1);
const image = ref(null);

const curr_yaer = computed(() => {
  const now = new Date();
  const currentYear = now.getFullYear();
  return currentYear;
});
// форм
const form_data = ref({
  title: "",
  description: "",
  meta_title: "",
  meta_description: "",
  status: false,
  region: null,
  district: null,
  settlement_type: null,
  settlement: null,
  full_adress: null,
  main_image: null,
  video_zen: null,
  video_rutube: null,
  link_to_ads: null,
  price: null,
  area_of_house: null,
  plot_area: null,
  bathroom_in_house: false,
  gaz: false,
  uid: null,
  //
  number_of_rooms: null,
  number_of_floors: null,
  sauna: false,
  plastic_windows: false,
  bus_stop: false,
  rail_station: false,
  distance_to_the_river: null,
  distance_to_the_lake: null,
  there_is_a_forest_nearby: false,
  distance_to_the_city: null,
  gas_heating: false,
  furnace_heating: false,
  sewerage: false,
  year_of_construction: null,
  wall_material_id: null,
  alarm_status: false,
});
</script>

<style lang="scss" scoped></style>
