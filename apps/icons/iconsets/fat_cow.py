from django.utils.translation import ugettext_lazy as _

from icons.literals import *
from icons.classes import IconSetBase


class IconSet(IconSetBase):
    name = 'fat_cow'
    label = _(u'Fat cow')
    directory = 'fat_cow'
    available_sizes = ['32x32', '16x16']
    dictionary = {
        ADD: 'add.png',
        APPLICATION_FORM: 'application_form.png',
        APPLICATION_FORM_DELETE: 'application_form_delete.png',
        APPLICATION_FORM_EDIT: 'application_form_edit.png',
        APPLICATION_FORM_ADD: 'application_form_add.png',
        APPLICATION_VIEW_ICONS: 'application_view_icons.png',
        APPLICATION_VIEW_ICONS: 'application_view_icons.png',
        ARROW_RIGHT: 'arrow_right.png',
        ARROW_TURN_RIGHT: 'arrow_turn_right.png',
        ARROW_TURN_LEFT: 'arrow_turn_left.png',
        ARROW_UP: 'arrow_up.png',
        BASKET: 'basket.png',
        BASKET_PUT: 'basket_put.png',
        BASKET_REMOVE: 'basket_remove.png',
        BIN: 'bin.png',
        BIN_CLOSED: 'bin_closed.png',
        BIN_EMPTY: 'bin_empty.png',
        BIN_EMPTY_OUT: ['bin_empty.png', 'arrow_turn_right.png'],
        BIN_MULTIPLE: ['bin_closed.png', 'bin_closed.png'],
        BIN_RECYCLE: ['bin.png', 'recycle.png'],
        BLACKBOARD_SUM: 'blackboard_sum.png',
        BOOK: 'book.png',
        BOOK_GO: 'book_go.png',
        BOOK_OPEN: 'book_open.png',
        BOOK_OPEN_PENCIL: ['book_open.png', 'pencil.png'],
        BUG: 'bug.png',
        BULLET_GO: 'bullet_go.png',
        CAMERA_DELETE: 'camera_delete.png',
        CD_BURN: 'cd_burn.png',
        COG: 'cog.png',
        COG_ADD: 'cog_add.png',
        COG_EDIT: 'cog_edit.png',
        COG_ERROR: 'cog_error.png',
        COG_DELETE: 'cog_delete.png',
        COG_HOURGLASS: ['cog.png', 'hourglass.png'],
        COMMENTS: 'comments.png',
        COMMENT_ADD: 'comment_add.png',
        COMMENT_DELETE: 'comment_delete.png',
        COMPUTER_KEY: 'computer_key.png',
        CONTROL_PLAY_BLUE: 'control_play_blue.png',
        CONTROL_STOP_BLUE: 'control_stop_blue.png',
        CROSS: 'cross.png',
        DATABASE: 'database.png',
        DATABASE_ADD: 'database_add.png',
        DATABASE_EDIT: 'database_edit.png',
        DATABASE_DELETE: 'database_delete.png',
        DATABASE_LIGHTNING: 'database_lightning.png',
        DELETE: 'delete.png',
        DISK: 'disk.png',
        DRAW_AIRBRUSH: 'draw_airbrush.png',
        DRIVE: 'drive.png',
        DRIVE_NETWORK: 'drive_network.png',
        DRIVE_USER: 'drive_user.png',
        DOCUMENT_SIGNATURE: 'document_signature.png',
        DOCUMENT_LOCK: ['page.png', 'lock.png'],
        EMAIL: 'email.png',
        ERROR: 'error.png',
        FIND: 'find.png',
        FIND_ADD: ['find.png', 'add.png'],
        FIND_ARROW_LEFT: ['find.png', 'arrow_left.png'],
        FOLDER: 'folder.png',
        FOLDERS: 'folders.png',
        FOLDER_ADD: 'folder_add.png',
        FOLDER_CAMERA: 'folder_camera.png',
        FOLDER_EDIT: 'folder_edit.png',
        FOLDER_DELETE: 'folder_delete.png',
        FOLDER_GO: 'folder_go.png',
        FOLDER_MAGNIFY: 'folder_magnify.png',
        FOLDER_PAGE: 'folder_page.png',
        FOLDER_USER: 'folder_user.png',
        GROUP: 'group.png',
        GROUP_ADD: 'group_add.png',
        GROUP_EDIT: 'group_edit.png',
        GROUP_DELETE: 'group_delete.png',
        GROUP_KEY: 'group_key.png',
        GROUP_LINK: 'group_link.png',
        GROUP_MEMBERS: ['group.png', 'arrow_refresh.png'],
        HELP: 'help.png',
        HOURGLASS: 'hourglass.png',
        HOUSE: 'house.png',
        IMAGE: 'image.png',
        IMAGES: 'images.png',
        INDEX: 'index.png',
        INFORMATION: 'information.png',
        KEY: 'key.png',
        KEY_GO: 'key_go.png',
        KEY_ADD: 'key_add.png',
        KEY_DELETE: 'key_delete.png',
        KEYBOARD: 'keyboard.png',
        LAYOUT: 'layout.png',
        LAYOUT_ADD: 'layout_add.png',
        LAYOUT_DELETE: 'layout_delete.png',
        LAYOUT_EDIT: 'layout_edit.png',
        LIGHTNING: 'lightning.png',
        LINK: 'link.png',
        LINK_ADD: 'link_add.png',
        LINK_EDIT: 'link_edit.png',
        LINK_DELETE: 'link_delete.png',
        LOCK: 'lock.png',
        LOCK_EDIT: 'lock_edit.png',
        LOCK_GO: 'lock_go.png',
        LORRY_GO: 'lorry_go.png',
        LORRY_DELETE: 'lorry_delete.png',
        MAGIC_WAND_2: 'magic_wand_2.png',
        MAGNIFIER: 'magnifier.png',
        MEDAL_GOLD: 'medal_gold_1.png',
        MEDAL_GOLD_ADD: 'medal_gold_add.png',
        MEDAL_GOLD_EDIT: ['medal_gold_1.png', 'pencil.png'],
        MEDAL_GOLD_DELETE: 'medal_gold_delete.png',
        NODE_TREE: 'node-tree.png',
        NODE_TREE_ADD: ['node-tree.png', 'add.png'],
        NODE_TREE_EDIT: ['node-tree.png', 'pencil.png'],
        NODE_TREE_DELETE: ['node-tree.png', 'delete.png'],
        PACKAGE: 'package.png',
        PAGE: 'page.png',
        PAGE_ADD: 'page_add.png',
        PAGE_COPY: 'page_copy.png',
        PAGE_GEAR: 'page_gear.png',
        PAGE_GO: 'page_go.png',
        PAGE_DELETE: 'page_delete.png',
        PAGE_EDIT: 'page_edit.png',
        PAGE_FIND: 'page_find.png',
        PAGE_LINK: 'page_link.png',
        PAGE_REFRESH: 'page_refresh.png',
        PAGE_SAVE: 'page_save.png',
        PAGE_WHITE: 'page_white.png',
        PAGE_WHITE_COPY: 'page_white_copy.png',
        PAGE_WHITE_CSHARP: 'page_white_csharp.png',
        PAGE_WHITE_EDIT: 'page_white_edit.png',
        PAGE_WHITE_GO: 'page_white_go.png',
        PAGE_WHITE_PICTURE: 'page_white_picture.png',
        PAGE_WHITE_TEXT: 'page_white_text.png',
        PAGE_WORLD: 'page_world.png',
        PENCIL_ADD: 'pencil_add.png',
        PENCIL_DELETE: 'pencil_delete.png',
        PICTURES: 'pictures.png',
        PILL: 'pill.png',
        PLUGIN: 'plugin.png',
        PRINTER: 'printer.png',
        PRINTER_EMPTY: 'printer_empty.png',
        QUESTION: 'question.png',
        RADIOACTIVITY: 'radioactivity.png',
        RAINBOW: 'rainbow.png',
        RESULTSET_FIRST: 'resultset_first.png',
        RESULTSET_LAST: 'resultset_last.png',
        RESULTSET_NEXT: 'resultset_next.png',
        RESULTSET_PREVIOUS: 'resultset_previous.png',
        ROUTING_TURNAROUND_RIGHT: 'routing_turnaround_right.png',
        SCRIPT: 'script.png',
        SERVER: 'server.png',
        STORAGE: 'storage.png',
        TAB: 'tab.png',
        TAB_ADD: 'tab_add.png',
        TAB_DELETE: 'tab_delete.png',
        TAB_EDIT: 'tab_edit.png',
        TAB_GO: 'tab_go.png', 
        TABLE: 'table.png',
        TABLE_ADD: 'table_add.png',
        TABLE_EDIT: 'table_edit.png',
        TABLE_DELETE: 'table_delete.png',
        TABLE_REFRESH: 'table_refresh.png',
        TABLE_RELATIONSHIP: 'table_relationship.png',
        TAG_BLUE: 'tag_blue.png',
        TAG_BLUE_ADD: 'tag_blue_add.png',
        TAG_BLUE_DELETE: 'tag_blue_delete.png',
        TAG_BLUE_EDIT: 'tag_blue_edit.png',
        TEXT_DROPCAPS: 'text_dropcaps.png',
        TEXT_SIGNATURE: 'text_signature.png',
        TEXT_STRIKETHROUGH: 'text_strikethrough.png',
        TEXTFIELD: 'textfield.png',
        TEXTFIELD_DELETE: 'textfield_delete.png',
        THEATER: 'theater.png',
        THEATER_ADD: ['theater.png', 'add.png'],
        THEATER_DELETE: ['theater.png', 'delete.png'],
        THEATER_EDIT: ['theater.png', 'pencil.png'],
        THEATER_GROUP: ['theater.png', 'group.png'],
        THEATER_KEY: ['theater.png', 'key.png'],
        TICK: 'tick.png',
        TIME: 'time.png',
        TIMELINE_MARKER: 'timeline_marker.png',
        TO_DO_LIST_CHEKED_1: 'to_do_list_cheked_1.png',
        TRAFFIC_LIGHTS_GREEN: 'traffic_lights_green.png',
        USER: 'user.png',
        USER_ADD:'user_add.png',
        USER_EDIT: 'user_edit.png',
        USER_DELETE: 'user_delete.png',
        USER_SILHOUETTE: 'user_silhouette.png',
        VCARD: 'vcard.png',
        VCARD_EDIT: 'vcard_edit.png',  
        WIZARD: 'wizard.png',
        WIZARD_ADD: ['wizard.png', 'add.png'],
        WIZARD_BOX_OPEN: ['wizard.png', 'box_open.png'],
        WIZARD_DELETE: ['wizard.png', 'delete.png'],
        WIZARD_DISK: ['wizard.png', 'disk.png'],
        WIZARD_EDIT: ['wizard.png', 'pencil.png'],
        WIZARD_FOLDER: ['wizard.png', 'folder.png'],
        WIZARD_LIGHTNING: ['wizard.png', 'lightning.png'],
        WIZARD_WORLD: ['wizard.png', 'world.png'],
        WORLD: 'world.png',
        WORLD_GO: 'world_go.png',
        WRENCH: 'wrench.png',
        XHTML: 'xhtml.png',
        XHTML_GO: 'xhtml_go.png',
        XHTML_ADD: 'xhtml_add.png',
        XHTML_DELETE: 'xhtml_delete.png',
        XHTML_EDIT: ['xhtml.png', 'pencil.png'],
        ZOOM: 'zoom.png',
        ZOOM_IN: 'zoom_in.png',
        ZOOM_OUT: 'zoom_out.png',
    }
