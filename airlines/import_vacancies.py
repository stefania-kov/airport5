{% extends 'base.html' %}
{% load static %}

{% block title %}Вакансии — ГосНИИмаш{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'portal/css/vacancies.css' %}?v={{ sv }}">
{% endblock %}

{% block page_data %}vacancies{% endblock %}

{% block content %}
<section class="page-hero">
    <div class="page-hero-inner">
        <div>
            <div class="page-hero-title">Вакансии</div>
            <div class="page-hero-subtitle">Открытые позиции компании — найдите подходящую возможность</div>
        </div>
        <div class="page-hero-icon" style="background: #1B3A8C"><i class="bi bi-briefcase-fill"></i></div>
    </div>
</section>

<section class="vac-section">
    <div class="container">
        <div class="filter-row">
            <div class="dept-dropdown" id="catDropdown">
                <button class="dept-dropdown-btn" id="catDropdownBtn">
                    <i class="bi bi-grid"></i>
                    <span id="catDropdownLabel">Все направления</span>
                    <i class="bi bi-chevron-down chevron"></i>
                </button>
                <div class="dept-dropdown-menu" id="catDropdownMenu">
                    <div class="dept-menu-item dept-menu-item--all active" data-category="all">
                        <span class="dept-menu-label"><i class="bi bi-grid"></i> Все вакансии</span>
                        <span class="dept-menu-count" id="countAll">0</span>
                    </div>
                    <div class="dept-dropdown-divider"></div>
                    <div class="dept-menu-item" data-category="it">
                        <span class="dept-menu-label"><i class="bi bi-cpu"></i> IT</span>
                        <span class="dept-menu-count" id="countIt">0</span>
                    </div>
                    <div class="dept-menu-item" data-category="engineering">
                        <span class="dept-menu-label"><i class="bi bi-gear-fill"></i> Инженерия</span>
                        <span class="dept-menu-count" id="countEngineering">0</span>
                    </div>
                    <div class="dept-menu-item" data-category="finance">
                        <span class="dept-menu-label"><i class="bi bi-currency-ruble"></i> Финансы</span>
                        <span class="dept-menu-count" id="countFinance">0</span>
                    </div>
                    <div class="dept-menu-item" data-category="hr">
                        <span class="dept-menu-label"><i class="bi bi-person-badge"></i> HR</span>
                        <span class="dept-menu-count" id="countHr">0</span>
                    </div>
                    <div class="dept-menu-item" data-category="management">
                        <span class="dept-menu-label"><i class="bi bi-diagram-3-fill"></i> Управление</span>
                        <span class="dept-menu-count" id="countManagement">0</span>
                    </div>
                </div>
            </div>
            <div class="pb-search">
                <i class="bi bi-search"></i>
                <input type="text" id="vacSearchInput" placeholder="Поиск по должности или отделу...">
            </div>
        </div>

        <div class="vac-grid" id="vacGrid"></div>
    </div>
</section>

<!-- МОДАЛЬНОЕ ОКНО -->
<div class="vac-modal" id="vacModal">
    <div class="vac-modal-content">
        <button class="vac-modal-close" id="vacModalClose"><i class="bi bi-x-lg"></i></button>

        <div class="vac-modal-header">
            <div class="vac-modal-icon" id="vacModalIcon"><i class="bi bi-briefcase-fill"></i></div>
            <div>
                <div class="vac-modal-title" id="vacModalTitle">Должность</div>
                <div class="vac-modal-meta-row">
                    <span class="vac-modal-dept" id="vacModalDept">Отдел</span>
                    <span class="vac-category-badge" id="vacModalBadge">Категория</span>
                </div>
            </div>
        </div>

        <div class="vac-modal-salary-block" id="vacModalSalaryBlock">
            <i class="bi bi-cash-stack"></i>
            <span id="vacModalSalary">—</span>
            <span class="vac-modal-type" id="vacModalType"></span>
        </div>

        <div class="vac-modal-body">
            <div class="vac-req-section">
                <div class="vac-req-title"><i class="bi bi-mortarboard-fill"></i> Образование</div>
                <div class="vac-req-text" id="vacModalEdu">—</div>
            </div>
            <div class="vac-req-section">
                <div class="vac-req-title"><i class="bi bi-clock-history"></i> Опыт работы</div>
                <div class="vac-req-text" id="vacModalExp">—</div>
            </div>
            <div class="vac-req-section">
                <div class="vac-req-title"><i class="bi bi-list-check"></i> Обязанности</div>
                <ul class="vac-duties-list" id="vacModalDuties"></ul>
            </div>
        </div>

        <div class="vac-modal-footer">
            <button class="vac-modal-btn vac-modal-btn-outline" id="vacModalCloseBtn">Закрыть</button>
        </div>
    </div>
</div>

{% endblock %}

{% block extra_js %}
<script>
    // Прямая вставка JSON строки
    const vacanciesDataJson = '{{ vacancies_json|escapejs }}';
    console.log('JSON строка длина:', vacanciesDataJson.length);
    
    // Парсим JSON
    let vacancies;
    try {
        vacancies = JSON.parse(vacanciesDataJson);
        console.log('Вакансий получено:', vacancies.length);
        console.log('Массив?', Array.isArray(vacancies));
    } catch(e) {
        console.error('Ошибка парсинга:', e);
        vacancies = [];
    }
    
    if (Array.isArray(vacancies) && vacancies.length) {
        window.vacanciesData = vacancies;
    } else {
        window.vacanciesData = [];
    }
</script>

<script src="{% static 'portal/js/vacancies.js' %}?v={{ sv }}"></script>
{% endblock %}
