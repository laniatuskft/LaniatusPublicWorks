class Globals:
    ITEM_SOCKET_REMAIN_SEC = 0

    ABSORB = 0
    COMBINE = 1

    ACCE_SLOT_LEFT = 0
    ACCE_SLOT_RIGHT = 1
    ACCE_SLOT_RESULT = 2
    ACCE_SLOT_MAX_NUM = 3


    QUICKSLOT_TYPE_NONE = 0
    QUICKSLOT_TYPE_ITEM = 1
    QUICKSLOT_TYPE_SKILL = 2
    QUICKSLOT_TYPE_COMMAND = 3
    QUICKSLOT_TYPE_MAX_NUM = 4

    SKILL_ATTR_TYPE_NORMAL = 1
    SKILL_ATTR_TYPE_MELEE = 2
    SKILL_ATTR_TYPE_RANGE = 3
    SKILL_ATTR_TYPE_MAGIC = 4

    SKILL_NORMAL = 0
    SKILL_MASTER = 1
    SKILL_GRAND_MASTER = 2
    SKILL_PERFECT_MASTER = 3
# Laniatus Games Studio Inc. |  TODO TASK: There is no equivalent in Python to templates on variables:
    singleton = None

    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if ! itertype
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define itertype(v) __typeof((v).begin())
    ##endif

    @staticmethod
    def stl_lowers(rstRet):
        i = 0
        while i < len(rstRet):
            rstRet[i] = tolower(rstRet[i])
            i += 1


    HEADER_GD_LOGIN = 1
    HEADER_GD_LOGOUT = 2
    HEADER_GD_PLAYER_LOAD = 3
    HEADER_GD_PLAYER_SAVE = 4
    HEADER_GD_PLAYER_CREATE = 5
    HEADER_GD_PLAYER_DELETE = 6
    HEADER_GD_LOGIN_KEY = 7
    HEADER_GD_BOOT = 9
    HEADER_GD_PLAYER_COUNT = 10
    HEADER_GD_QUEST_SAVE = 11
    HEADER_GD_SAFEBOX_LOAD = 12
    HEADER_GD_SAFEBOX_SAVE = 13
    HEADER_GD_SAFEBOX_CHANGE_SIZE = 14
    HEADER_GD_EMPIRE_SELECT = 15
    HEADER_GD_SAFEBOX_CHANGE_PASSWORD = 16
    HEADER_GD_SAFEBOX_CHANGE_PASSWORD_SECOND = 17
    HEADER_GD_DIRECT_ENTER = 18
    HEADER_GD_GUILD_SKILL_UPDATE = 19
    HEADER_GD_GUILD_EXP_UPDATE = 20
    HEADER_GD_GUILD_ADD_MEMBER = 21
    HEADER_GD_GUILD_REMOVE_MEMBER = 22
    HEADER_GD_GUILD_CHANGE_GRADE = 23
    HEADER_GD_GUILD_CHANGE_MEMBER_DATA = 24
    HEADER_GD_GUILD_DISBAND = 25
    HEADER_GD_GUILD_WAR = 26
    HEADER_GD_GUILD_WAR_SCORE = 27
    HEADER_GD_GUILD_CREATE = 28
    HEADER_GD_ITEM_SAVE = 30
    HEADER_GD_ITEM_DESTROY = 31
    HEADER_GD_ADD_AFFECT = 32
    HEADER_GD_REMOVE_AFFECT = 33
    HEADER_GD_HIGHSCORE_REGISTER = 34
    HEADER_GD_ITEM_FLUSH = 35
    HEADER_GD_PARTY_CREATE = 36
    HEADER_GD_PARTY_DELETE = 37
    HEADER_GD_PARTY_ADD = 38
    HEADER_GD_PARTY_REMOVE = 39
    HEADER_GD_PARTY_STATE_CHANGE = 40
    HEADER_GD_PARTY_HEAL_USE = 41
    HEADER_GD_FLUSH_CACHE = 42
    HEADER_GD_RELOAD_PROTO = 43
    HEADER_GD_CHANGE_NAME = 44
    HEADER_GD_GUILD_CHANGE_LADDER_POINT = 46
    HEADER_GD_GUILD_USE_SKILL = 47
    HEADER_GD_REQUEST_EMPIRE_PRIV = 48
    HEADER_GD_REQUEST_GUILD_PRIV = 49
    HEADER_GD_GUILD_DEPOSIT_MONEY = 51
    HEADER_GD_GUILD_WITHDRAW_MONEY = 52
    HEADER_GD_GUILD_WITHDRAW_MONEY_GIVE_REPLY = 53
    HEADER_GD_REQUEST_CHARACTER_PRIV = 54
    HEADER_GD_SET_EVENT_FLAG = 55
    HEADER_GD_PARTY_SET_MEMBER_LEVEL = 56
    HEADER_GD_GUILD_WAR_BET = 57
    HEADER_GD_CREATE_OBJECT = 60
    HEADER_GD_DELETE_OBJECT = 61
    HEADER_GD_UPDATE_LAND = 62
    HEADER_GD_MARRIAGE_ADD = 70
    HEADER_GD_MARRIAGE_UPDATE = 71
    HEADER_GD_MARRIAGE_REMOVE = 72
    HEADER_GD_WEDDING_REQUEST = 73
    HEADER_GD_WEDDING_READY = 74
    HEADER_GD_WEDDING_END = 75
    HEADER_GD_AUTH_LOGIN = 100
    HEADER_GD_LOGIN_BY_KEY = 101
    HEADER_GD_MALL_LOAD = 107
    HEADER_GD_MYSHOP_PRICELIST_UPDATE = 108
    HEADER_GD_MYSHOP_PRICELIST_REQ = 109
    HEADER_GD_BLOCK_CHAT = 110
    HEADER_GD_RELOAD_ADMIN = 115
    HEADER_GD_BREAK_MARRIAGE = 116
    HEADER_GD_REQ_CHANGE_GUILD_MASTER = 129
    HEADER_GD_REQ_SPARE_ITEM_ID_RANGE = 130
    HEADER_GD_UPDATE_HORSE_NAME = 131
    HEADER_GD_REQ_HORSE_NAME = 132
    HEADER_GD_DC = 133
    HEADER_GD_VALID_LOGOUT = 134
    HEADER_GD_REQUEST_CHARGE_CASH = 137
    HEADER_GD_DELETE_AWARDID = 138
    HEADER_GD_UPDATE_CHANNELSTATUS = 139
    HEADER_GD_REQUEST_CHANNELSTATUS = 140
    int #if __MULTI_LANGUAGE_SYSTEM__ = 141
    HEADER_GD_REQUEST_CHANGE_LANGUAGE = 146
    int #endif = 147
    int #if (not _IMPROVED_PACKET_ENCRYPTION_) = 148
    HEADER_GD_SHUTDOWN = 149
    int #endif = 150
    HEADER_GD_SETUP = 0xff
    HEADER_DG_NOTICE = 1
    HEADER_DG_LOGIN_SUCCESS = 30
    HEADER_DG_LOGIN_NOT_EXIST = 31
    HEADER_DG_LOGIN_WRONG_PASSWD = 33
    HEADER_DG_LOGIN_ALREADY = 34
    HEADER_DG_PLAYER_LOAD_SUCCESS = 35
    HEADER_DG_PLAYER_LOAD_FAILED = 36
    HEADER_DG_PLAYER_CREATE_SUCCESS = 37
    HEADER_DG_PLAYER_CREATE_ALREADY = 38
    HEADER_DG_PLAYER_CREATE_FAILED = 39
    HEADER_DG_PLAYER_DELETE_SUCCESS = 40
    HEADER_DG_PLAYER_DELETE_FAILED = 41
    HEADER_DG_ITEM_LOAD = 42
    HEADER_DG_BOOT = 43
    HEADER_DG_QUEST_LOAD = 44
    HEADER_DG_SAFEBOX_LOAD = 45
    HEADER_DG_SAFEBOX_CHANGE_SIZE = 46
    HEADER_DG_SAFEBOX_WRONG_PASSWORD = 47
    HEADER_DG_SAFEBOX_CHANGE_PASSWORD_ANSWER = 48
    HEADER_DG_EMPIRE_SELECT = 49
    HEADER_DG_AFFECT_LOAD = 50
    HEADER_DG_MALL_LOAD = 51
    HEADER_DG_DIRECT_ENTER = 55
    HEADER_DG_GUILD_SKILL_UPDATE = 56
    HEADER_DG_GUILD_SKILL_RECHARGE = 57
    HEADER_DG_GUILD_EXP_UPDATE = 58
    HEADER_DG_PARTY_CREATE = 59
    HEADER_DG_PARTY_DELETE = 60
    HEADER_DG_PARTY_ADD = 61
    HEADER_DG_PARTY_REMOVE = 62
    HEADER_DG_PARTY_STATE_CHANGE = 63
    HEADER_DG_PARTY_HEAL_USE = 64
    HEADER_DG_PARTY_SET_MEMBER_LEVEL = 65
    HEADER_DG_TIME = 90
    HEADER_DG_ITEM_ID_RANGE = 91
    HEADER_DG_GUILD_ADD_MEMBER = 92
    HEADER_DG_GUILD_REMOVE_MEMBER = 93
    HEADER_DG_GUILD_CHANGE_GRADE = 94
    HEADER_DG_GUILD_CHANGE_MEMBER_DATA = 95
    HEADER_DG_GUILD_DISBAND = 96
    HEADER_DG_GUILD_WAR = 97
    HEADER_DG_GUILD_WAR_SCORE = 98
    HEADER_DG_GUILD_TIME_UPDATE = 99
    HEADER_DG_GUILD_LOAD = 100
    HEADER_DG_GUILD_LADDER = 101
    HEADER_DG_GUILD_SKILL_USABLE_CHANGE = 102
    HEADER_DG_GUILD_MONEY_CHANGE = 103
    HEADER_DG_GUILD_WITHDRAW_MONEY_GIVE = 104
    HEADER_DG_SET_EVENT_FLAG = 105
    HEADER_DG_GUILD_WAR_RESERVE_ADD = 106
    HEADER_DG_GUILD_WAR_RESERVE_DEL = 107
    HEADER_DG_GUILD_WAR_BET = 108
    HEADER_DG_RELOAD_PROTO = 120
    HEADER_DG_CHANGE_NAME = 121
    HEADER_DG_AUTH_LOGIN = 122
    HEADER_DG_CHANGE_EMPIRE_PRIV = 124
    HEADER_DG_CHANGE_GUILD_PRIV = 125
    HEADER_DG_CHANGE_CHARACTER_PRIV = 127
    HEADER_DG_CREATE_OBJECT = 140
    HEADER_DG_DELETE_OBJECT = 141
    HEADER_DG_UPDATE_LAND = 142
    HEADER_DG_MARRIAGE_ADD = 150
    HEADER_DG_MARRIAGE_UPDATE = 151
    HEADER_DG_MARRIAGE_REMOVE = 152
    HEADER_DG_WEDDING_REQUEST = 153
    HEADER_DG_WEDDING_READY = 154
    HEADER_DG_WEDDING_START = 155
    HEADER_DG_WEDDING_END = 156
    HEADER_DG_MYSHOP_PRICELIST_RES = 157
    HEADER_DG_RELOAD_ADMIN = 158
    HEADER_DG_BREAK_MARRIAGE = 159
    HEADER_DG_ACK_CHANGE_GUILD_MASTER = 173
    HEADER_DG_ACK_SPARE_ITEM_ID_RANGE = 174
    HEADER_DG_UPDATE_HORSE_NAME = 175
    HEADER_DG_ACK_HORSE_NAME = 176
    HEADER_DG_NEED_LOGIN_LOG = 177
    HEADER_DG_RESULT_CHARGE_CASH = 179
    HEADER_DG_ITEMAWARD_INFORMER = 180
    HEADER_DG_RESPOND_CHANNELSTATUS = 181
    int #if (not _IMPROVED_PACKET_ENCRYPTION_) = 182
    HEADER_DG_SHUTDOWN = 184
    int #endif = 185
    HEADER_DG_MAP_LOCATIONS = 0xfe
    HEADER_DG_P2P = 0xff
    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = (strtol(in_, None, 10) != 0)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = (char) strtol(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = byte(int(strtoul(in_, None, 10)))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = short(int(strtol(in_, None, 10)))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = strtoul(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = int(strtol(in_, None, 10))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = strtoul(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = int(strtol(in_, None, 10))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = strtoul(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = int(strtoull(in_, None, 10))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = float(strtof(in_, None))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = float(strtod(in_, None))
        return True

    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if __FreeBSD__
    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = float(strtold(in_, None))
        return True
    ##endif
