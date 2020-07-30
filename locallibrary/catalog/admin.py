from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'borrower')

    fieldsets = (
        (None, {
            "fields": (
                ('book', 'imprint', 'id')
            ),
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )
    


admin.site.register(Genre)