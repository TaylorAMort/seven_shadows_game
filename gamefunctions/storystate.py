class StoryState:
    def __init__(self):
        self.scene_rounds = {}
        self.choices = set()

    def enter_scene(self, scene_name):
        if scene_name not in self.scene_rounds:
            self.scene_rounds[scene_name] = 0
        self.scene_rounds[scene_name] += 1
    
    def rounds(self, scene_name):
        return self.scene_rounds.get(scene_name, 0)
    
    def make_choice(self, choice_name):
        self.choices.add(choice_name)

    def has_made_choice(self, choice_name):
        return choice_name in self.choices