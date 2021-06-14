class SkillImpactEffect:
    """
    技能影响效果

    """

    def impact(self, *args):
        raise NotImplementedError()

class DamageEffect(SkillImpactEffect):
    def __init__(self, hp):
        self.hp = hp

    def impact(self):
        print("扣血%d" % self.hp)

class LowerDeffense(SkillImpactEffect):
    def __init__(self, deffense, time):
        self.deffense = deffense
        self.time = time

    def impact(self):
        print("降低防御力%s,suatain %d 秒" % (self.deffense, self.time))

class DizzinessEffects(SkillImpactEffect):
    def __init__(self, time):
        self.time = time

    def impact(self):
        print("眩晕 %d 秒" % (self.time))

class SkillDeployer:
    """
    技能释放器 ：1，加载配置文件   2，创建效果对象->生成技能（执行效果）
    """

    def __init__(self, name):
        self.__name = name
        self.__dic_skill_config = self.__load_config_file()
        self.__effect_objects = self.__create_effect_objects()

    def __load_config_file(self):
        return {
            "降龙十八掌": ["DamageEffect(200)", "LowerDeffense(-50,5)",
                      "DizzinessEffects(2)"],
            "六脉神剑": ["DamageEffect(50)", "LowerDeffense(-10,2)"]
        }

    def __create_effect_objects(self):
        ans = []
        for item in self.__dic_skill_config[self.__name]:
            eval_object = eval(item)
            ans.append(eval_object)
        return ans

    def generate_skills(self):
        for item in self.__effect_objects:
            item.impact()

manager = SkillDeployer("降龙十八掌")
manager.generate_skills()
